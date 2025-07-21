from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ia_vendedora.db")

# Para Railway/PostgreSQL, ajustar URL se necessário
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuração específica para PostgreSQL vs SQLite
if DATABASE_URL.startswith("postgresql://"):
    engine = create_engine(DATABASE_URL)
else:
    # SQLite para desenvolvimento local
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modelos SQLAlchemy para o banco de dados

class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    category = Column(String, index=True)
    stock = Column(Integer, default=0)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AIConfigDB(Base):
    __tablename__ = "ai_configs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    personality = Column(Text)
    greeting_message = Column(Text)
    sales_approach = Column(Text)
    tone = Column(String)
    language = Column(String, default="pt-br")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Função para criar as tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

