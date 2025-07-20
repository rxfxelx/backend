from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.connection import Base


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    category = Column(String(100), nullable=True)
    features = Column(Text, nullable=True)  # JSON string ou texto livre
    benefits = Column(Text, nullable=True)
    target_audience = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Chave estrangeira
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relacionamentos
    owner = relationship("User", back_populates="products")

