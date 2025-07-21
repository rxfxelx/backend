import openai
import os
from typing import List, Optional
from .models import Product, AIConfig, ChatResponse
from .database import get_db, ProductDB, AIConfigDB
from sqlalchemy.orm import Session

class AIVendedora:
    def __init__(self):
        # Configuração da OpenAI
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
    
    def get_ai_config(self, db: Session) -> Optional[AIConfig]:
        """Busca a configuração da IA no banco de dados"""
        config_db = db.query(AIConfigDB).first()
        if config_db:
            return AIConfig.from_orm(config_db)
        return None
    
    def get_products_context(self, db: Session) -> str:
        """Gera contexto dos produtos para a IA"""
        products = db.query(ProductDB).all()
        if not products:
            return "Não há produtos cadastrados no momento."
        
        context = "Produtos disponíveis:\n"
        for product in products:
            context += f"- {product.name}: {product.description} | Preço: R$ {product.price:.2f} | Estoque: {product.stock} unidades\n"
        
        return context
    
    def create_system_prompt(self, ai_config: AIConfig, products_context: str) -> str:
        """Cria o prompt do sistema para a IA"""
        base_prompt = f"""
Você é {ai_config.name}, uma vendedora virtual especializada em ajudar clientes.

PERSONALIDADE: {ai_config.personality}

TOM DE VOZ: {ai_config.tone}

ABORDAGEM DE VENDAS: {ai_config.sales_approach}

MENSAGEM DE SAUDAÇÃO: {ai_config.greeting_message}

PRODUTOS DISPONÍVEIS:
{products_context}

INSTRUÇÕES:
1. Sempre seja educada e prestativa
2. Conheça bem os produtos e suas características
3. Faça perguntas para entender as necessidades do cliente
4. Sugira produtos adequados baseado no que o cliente busca
5. Informe preços e disponibilidade quando relevante
6. Mantenha o foco em ajudar o cliente a encontrar o que precisa
7. Se não souber algo sobre um produto, seja honesta
8. Sempre termine oferecendo mais ajuda

Responda sempre em português brasileiro de forma natural e conversacional.
"""
        return base_prompt
    
    def chat(self, message: str, db: Session, user_id: Optional[str] = None) -> ChatResponse:
        """Processa uma mensagem do chat e retorna a resposta da IA"""
        try:
            # Busca configuração da IA
            ai_config = self.get_ai_config(db)
            if not ai_config:
                # Configuração padrão se não houver nenhuma
                ai_config = AIConfig(
                    id=1,
                    name="Vendedora Virtual",
                    personality="Amigável, profissional e prestativa",
                    greeting_message="Olá! Como posso ajudá-lo hoje?",
                    sales_approach="Consultiva, focando nas necessidades do cliente",
                    tone="Amigável e profissional",
                    language="pt-br",
                    created_at=None,
                    updated_at=None
                )
            
            # Busca contexto dos produtos
            products_context = self.get_products_context(db)
            
            # Cria o prompt do sistema
            system_prompt = self.create_system_prompt(ai_config, products_context)
            
            # Chama a API da OpenAI
            client = openai.OpenAI(api_key=openai.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Identifica produtos mencionados (implementação simples)
            products_mentioned = self.identify_mentioned_products(ai_response, db)
            
            return ChatResponse(
                response=ai_response,
                products_mentioned=products_mentioned
            )
            
        except Exception as e:
            return ChatResponse(
                response=f"Desculpe, ocorreu um erro. Tente novamente em alguns instantes. Erro: {str(e)}",
                products_mentioned=[]
            )
    
    def identify_mentioned_products(self, response: str, db: Session) -> List[Product]:
        """Identifica produtos mencionados na resposta da IA"""
        products = db.query(ProductDB).all()
        mentioned = []
        
        response_lower = response.lower()
        for product in products:
            if product.name.lower() in response_lower:
                mentioned.append(Product.from_orm(product))
        
        return mentioned

