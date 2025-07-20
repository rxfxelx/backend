from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.models.product import Product
from app.schemas.webhook import WebhookMessage, WebhookResponse
from app.services.openai_service import generate_ai_response

router = APIRouter(prefix="/webhook", tags=["Webhook"])


@router.post("/", response_model=WebhookResponse)
async def process_webhook_message(
    webhook_data: WebhookMessage,
    db: Session = Depends(get_db)
):
    """
    Processa mensagem recebida via webhook e retorna resposta da IA
    """
    # Buscar usuário
    user = db.query(User).filter(User.id == webhook_data.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    # Buscar produtos do usuário
    products = db.query(Product).filter(Product.owner_id == user.id).all()
    
    # Gerar resposta da IA
    ai_response = generate_ai_response(user, products, webhook_data.mensagem)
    
    return WebhookResponse(
        resposta=ai_response,
        user_id=webhook_data.user_id
    )

