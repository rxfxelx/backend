from openai import OpenAI
from typing import List
from app.config import settings
from app.models.user import User
from app.models.product import Product

# Configurar cliente OpenAI
client = OpenAI(api_key=settings.openai_api_key)


def generate_ai_response(user: User, products: List[Product], message: str) -> str:
    """
    Gera resposta da IA baseada nos produtos do usuário e no tom configurado
    """
    if not settings.openai_api_key:
        return "Erro: Chave da API OpenAI não configurada."
    
    # Construir contexto dos produtos
    products_context = ""
    if products:
        products_context = "Produtos disponíveis:\n"
        for product in products:
            products_context += f"- {product.name}"
            if product.description:
                products_context += f": {product.description}"
            if product.price:
                products_context += f" (Preço: R$ {product.price})"
            if product.features:
                products_context += f"\n  Características: {product.features}"
            if product.benefits:
                products_context += f"\n  Benefícios: {product.benefits}"
            if product.target_audience:
                products_context += f"\n  Público-alvo: {product.target_audience}"
            products_context += "\n\n"
    else:
        products_context = "Nenhum produto cadastrado ainda."
    
    # Construir prompt completo
    system_prompt = f"""
Você é um assistente de vendas da empresa {user.company_name or 'nossa empresa'}.

Tom da conversa: {user.ai_tone}

{products_context}

Instruções:
- Responda sempre de forma profissional e prestativa
- Use as informações dos produtos para responder perguntas
- Se a pergunta não for sobre os produtos, seja educado mas direcione para os produtos
- Mantenha o tom definido pelo usuário
- Seja conciso mas informativo
"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modelo mais barato
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

