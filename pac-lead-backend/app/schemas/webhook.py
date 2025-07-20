from pydantic import BaseModel


class WebhookMessage(BaseModel):
    mensagem: str
    user_id: int


class WebhookResponse(BaseModel):
    resposta: str
    user_id: int

