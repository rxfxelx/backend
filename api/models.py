from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Modelos Pydantic para validação de dados

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category: str
    stock: int = 0
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    stock: Optional[int] = None
    image_url: Optional[str] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AIConfigBase(BaseModel):
    name: str
    personality: str
    greeting_message: str
    sales_approach: str
    tone: str
    language: str = "pt-br"

class AIConfigCreate(AIConfigBase):
    pass

class AIConfigUpdate(BaseModel):
    name: Optional[str] = None
    personality: Optional[str] = None
    greeting_message: Optional[str] = None
    sales_approach: Optional[str] = None
    tone: Optional[str] = None
    language: Optional[str] = None

class AIConfig(AIConfigBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    products_mentioned: List[Product] = []

