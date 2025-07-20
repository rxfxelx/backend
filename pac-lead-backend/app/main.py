from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base
from app.routers import auth_router, products_router, webhook_router
from app.config import settings

# Criar tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="Pac Lead API",
    description="API para plataforma SaaS de IA de vendas personalizada",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(webhook_router)


@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Bem-vindo à API Pac Lead",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Endpoint de verificação de saúde da API"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

