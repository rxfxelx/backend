from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from dotenv import load_dotenv

# Importações locais
from .models import (
    Product, ProductCreate, ProductUpdate,
    AIConfig, AIConfigCreate, AIConfigUpdate,
    ChatMessage, ChatResponse
)
from .database import (
    get_db, create_tables, ProductDB, AIConfigDB
)
from .ai_service import AIVendedora

# Carrega variáveis de ambiente
load_dotenv()

# Cria as tabelas no banco de dados
create_tables()

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="IA Vendedora API",
    description="API para gerenciar produtos e configurações da IA vendedora",
    version="1.0.0"
)

# Configuração CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React local
        "http://localhost:5173",  # Vite local
        "https://*.vercel.app",   # Frontend no Vercel
        "*"  # Para desenvolvimento - remover em produção
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa o serviço da IA
ai_vendedora = AIVendedora()

# ==================== ROTAS DE PRODUTOS ====================

@app.get("/api/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    """Lista todos os produtos"""
    products = db.query(ProductDB).all()
    return products

@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Busca um produto específico"""
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

@app.post("/api/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Cria um novo produto"""
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/api/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """Atualiza um produto existente"""
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Atualiza apenas os campos fornecidos
    update_data = product.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Deleta um produto"""
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Produto deletado com sucesso"}

# ==================== ROTAS DE CONFIGURAÇÃO DA IA ====================

@app.get("/api/ai-config", response_model=Optional[AIConfig])
def get_ai_config(db: Session = Depends(get_db)):
    """Busca a configuração atual da IA"""
    config = db.query(AIConfigDB).first()
    return config

@app.post("/api/ai-config", response_model=AIConfig, status_code=status.HTTP_201_CREATED)
def create_ai_config(config: AIConfigCreate, db: Session = Depends(get_db)):
    """Cria ou atualiza a configuração da IA"""
    # Remove configuração existente (só permitimos uma configuração)
    db.query(AIConfigDB).delete()
    
    db_config = AIConfigDB(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

@app.put("/api/ai-config/{config_id}", response_model=AIConfig)
def update_ai_config(config_id: int, config: AIConfigUpdate, db: Session = Depends(get_db)):
    """Atualiza a configuração da IA"""
    db_config = db.query(AIConfigDB).filter(AIConfigDB.id == config_id).first()
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuração não encontrada")
    
    # Atualiza apenas os campos fornecidos
    update_data = config.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_config, field, value)
    
    db.commit()
    db.refresh(db_config)
    return db_config

# ==================== ROTAS DO CHAT ====================

@app.post("/api/chat", response_model=ChatResponse)
def chat_with_ai(message: ChatMessage, db: Session = Depends(get_db)):
    """Envia uma mensagem para a IA vendedora"""
    try:
        response = ai_vendedora.chat(message.message, db, message.user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no chat: {str(e)}")

# ==================== ROTAS DE INFORMAÇÕES ====================

@app.get("/api/health")
def health_check():
    """Verifica se a API está funcionando"""
    return {"status": "ok", "message": "IA Vendedora API está funcionando"}

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    """Retorna estatísticas básicas"""
    total_products = db.query(ProductDB).count()
    has_ai_config = db.query(AIConfigDB).first() is not None
    
    return {
        "total_products": total_products,
        "has_ai_config": has_ai_config,
        "api_version": "1.0.0"
    }

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "IA Vendedora API - Acesse /docs para ver a documentação"}

# Para desenvolvimento local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

