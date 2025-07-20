# Pac Lead API

API backend para plataforma SaaS de IA de vendas personalizada. Permite que cada cliente tenha sua própria IA de vendas que responde automaticamente com base em seus produtos cadastrados.

## Funcionalidades

- ✅ Cadastro e login de usuários com autenticação JWT
- ✅ CRUD completo de produtos (cada usuário acessa apenas seus produtos)
- ✅ Configuração personalizada do "tom da IA"
- ✅ Webhook para receber mensagens e gerar respostas via OpenAI
- ✅ Documentação automática da API (Swagger/OpenAPI)
- ✅ Suporte a CORS para integração com frontend

## Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados (pode ser facilmente alterado)
- **JWT** - Autenticação via tokens
- **OpenAI API** - Geração de respostas inteligentes
- **Pydantic** - Validação de dados

## Instalação

1. Clone o repositório e navegue até a pasta:
```bash
cd pac-lead-backend
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo `.env`:
```env
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./pac_lead.db
OPENAI_API_KEY=sua-chave-openai-aqui
```

4. Execute a aplicação:
```bash
python run.py
```

A API estará disponível em: http://localhost:8000

## Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints Principais

### Autenticação
- `POST /auth/register` - Cadastro de usuário
- `POST /auth/login` - Login e obtenção de token
- `GET /auth/me` - Informações do usuário atual
- `PUT /auth/me` - Atualizar perfil do usuário

### Produtos
- `POST /products/` - Criar produto
- `GET /products/` - Listar produtos do usuário
- `GET /products/{id}` - Obter produto específico
- `PUT /products/{id}` - Atualizar produto
- `DELETE /products/{id}` - Remover produto

### Webhook
- `POST /webhook/` - Processar mensagem e gerar resposta da IA

## Exemplo de Uso do Webhook

```bash
curl -X POST "http://localhost:8000/webhook/" \
  -H "Content-Type: application/json" \
  -d '{
    "mensagem": "Quais produtos vocês têm disponíveis?",
    "user_id": 1
  }'
```

Resposta:
```json
{
  "resposta": "Olá! Temos diversos produtos disponíveis...",
  "user_id": 1
}
```

## Estrutura do Projeto

```
pac-lead-backend/
├── app/
│   ├── routers/          # Endpoints da API
│   ├── models/           # Modelos do banco de dados
│   ├── schemas/          # Schemas Pydantic
│   ├── database/         # Configuração do banco
│   ├── services/         # Serviços (OpenAI, etc.)
│   ├── auth.py          # Sistema de autenticação
│   ├── config.py        # Configurações
│   └── main.py          # Aplicação principal
├── requirements.txt      # Dependências
├── .env                 # Variáveis de ambiente
├── run.py              # Script de inicialização
└── README.md           # Documentação
```

## Próximos Passos

Esta API está preparada para integração com:
- Frontend React
- APIs de WhatsApp (como WhatsApp Business API)
- Outros sistemas de mensageria

Para produção, considere:
- Usar PostgreSQL ao invés de SQLite
- Configurar variáveis de ambiente adequadas
- Implementar rate limiting
- Adicionar logs estruturados
- Configurar monitoramento

