from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[Decimal] = None
    category: Optional[str] = None
    features: Optional[str] = None
    benefits: Optional[str] = None
    target_audience: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    category: Optional[str] = None
    features: Optional[str] = None
    benefits: Optional[str] = None
    target_audience: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

