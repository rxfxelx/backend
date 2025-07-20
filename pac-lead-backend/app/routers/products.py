from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.auth import get_current_user

router = APIRouter(prefix="/products", tags=["Produtos"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cria um novo produto para o usuário atual"""
    db_product = Product(**product.dict(), owner_id=current_user.id)
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product


@router.get("/", response_model=List[ProductResponse])
async def list_products(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Lista todos os produtos do usuário atual"""
    products = db.query(Product).filter(Product.owner_id == current_user.id).all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtém um produto específico do usuário atual"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.owner_id == current_user.id
    ).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_update: ProductUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Atualiza um produto do usuário atual"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.owner_id == current_user.id
    ).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    update_data = product_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(product, field, value)
    
    db.commit()
    db.refresh(product)
    
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Remove um produto do usuário atual"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.owner_id == current_user.id
    ).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    db.delete(product)
    db.commit()
    
    return None

