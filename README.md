# IA Vendedora - Sistema Completo

## Visão Geral

Este é um sistema completo de IA vendedora que permite:
- Gerenciar produtos através de um painel web
- Configurar o comportamento da IA vendedora
- Interagir com a IA através de um chat
- Deploy gratuito no Railway (backend) e Vercel (frontend)

## Arquitetura

- **Backend:** FastAPI (Python) - APIs REST
- **Frontend:** HTML/CSS/JavaScript (a ser gerado por IA)
- **Banco de Dados:** PostgreSQL (recomendado para Railway)
- **IA:** OpenAI GPT-3.5-turbo
- **Deploy:** Railway (backend) e Vercel (frontend)

## Estrutura do Projeto

```
ia-vendedora/
├── api/                    # Backend FastAPI
│   ├── index.py           # Aplicação principal
│   ├── models.py          # Modelos Pydantic
│   ├── database.py        # Configuração do banco
│   └── ai_service.py      # Serviço da IA
├── requirements.txt       # Dependências Python
├── vercel.json           # Configuração do Vercel (para frontend)
├── railway.json          # Configuração do Railway (para backend)
├── .env.example          # Exemplo de variáveis de ambiente
├── PROMPT_FRONTEND.md    # Prompt para gerar frontend
└── README.md             # Esta documentação
```

## Configuração e Deploy

### 1. Preparação do Ambiente

1. Clone ou baixe este projeto
2. Crie uma conta no [Railway](https://railway.app) (para o backend)
3. Crie uma conta no [Vercel](https://vercel.com) (para o frontend)
4. Obtenha uma chave da API da OpenAI em [OpenAI Platform](https://platform.openai.com)

### 2. Deploy do Backend no Railway

1. Crie um novo projeto no Railway e conecte seu repositório GitHub.
2. O Railway detectará automaticamente o `railway.json` e o `requirements.txt`.
3. **Variáveis de Ambiente no Railway:**
   - `OPENAI_API_KEY`: Sua chave da API da OpenAI.
   - `DATABASE_URL`: A URL de conexão do seu banco de dados PostgreSQL (o Railway pode provisionar um para você).
4. O Railway fará o deploy automaticamente. A URL da sua API será algo como `https://<seu-projeto>-<id>.up.railway.app`.

### 3. Deploy do Frontend no Vercel

1. Use o `PROMPT_FRONTEND.md` para gerar o código do seu frontend.
2. Crie um novo projeto no Vercel e conecte o repositório do seu frontend.
3. No código do frontend, substitua a `API_BASE_URL` pela URL do seu backend no Railway.
4. O Vercel fará o deploy automaticamente. A URL do seu frontend será algo como `https://<seu-frontend>.vercel.app`.

## APIs Disponíveis

### Base URL
```
https://<seu-projeto>-<id>.up.railway.app/api
```

### Produtos
- `GET /api/products` - Listar produtos
- `POST /api/products` - Criar produto
- `GET /api/products/{id}` - Buscar produto
- `PUT /api/products/{id}` - Atualizar produto
- `DELETE /api/products/{id}` - Deletar produto

### Configuração da IA
- `GET /api/ai-config` - Buscar configuração
- `POST /api/ai-config` - Criar/atualizar configuração
- `PUT /api/ai-config/{id}` - Atualizar configuração

### Chat
- `POST /api/chat` - Enviar mensagem para IA

### Utilitários
- `GET /api/health` - Status da API
- `GET /api/stats` - Estatísticas do sistema

## Gerando o Frontend

Use o arquivo `PROMPT_FRONTEND.md` em uma IA de frontend (como Claude, ChatGPT, ou v0.dev) para gerar automaticamente a interface web completa.

O prompt inclui:
- Especificações técnicas detalhadas
- Documentação completa das APIs
- Design system e paleta de cores
- Exemplos de código
- Estrutura de arquivos
- Requisitos de responsividade

## Funcionalidades

### Gerenciamento de Produtos
- Adicionar, editar e remover produtos
- Categorização e controle de estoque
- Upload de imagens (via URL)
- Busca e filtros

### Configuração da IA
- Personalizar nome da vendedora
- Definir personalidade e tom de voz
- Configurar mensagens de saudação
- Ajustar abordagem de vendas

### Chat com IA
- Interface de chat em tempo real
- IA contextualizada com produtos
- Identificação de produtos mencionados
- Histórico de conversas

## Desenvolvimento Local

### Requisitos
- Python 3.9+
- pip

### Instalação
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com sua chave da OpenAI e DATABASE_URL (se usar PostgreSQL localmente)

# Executar localmente
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

### Testando as APIs
Acesse `http://localhost:8000/docs` para ver a documentação interativa das APIs.

## Personalização

### Modificando a IA
Edite o arquivo `api/ai_service.py` para:
- Alterar o modelo da OpenAI
- Modificar prompts do sistema
- Adicionar novas funcionalidades
- Integrar outros serviços de IA

### Adicionando Funcionalidades
- Novos endpoints em `api/index.py`
- Novos modelos em `api/models.py`
- Novas tabelas em `api/database.py`

## Limitações e Considerações

### Banco de Dados
- SQLite funciona para desenvolvimento local
- Para produção no Railway, **é essencial usar um banco de dados externo (PostgreSQL)**
- O Railway pode provisionar um PostgreSQL para você

### Escalabilidade
- Para alto volume, considere:
  - Cache (Redis)
  - CDN para imagens
  - Rate limiting

### Segurança
- Adicione autenticação para produção
- Valide todas as entradas
- Configure CORS adequadamente
- Use HTTPS sempre

## Próximos Passos

1. **Gere o frontend** usando o prompt fornecido
2. **Teste o sistema** completo
3. **Personalize** conforme suas necessidades
4. **Configure** banco de dados externo no Railway
5. **Adicione** autenticação se for usar em produção

## Suporte

Para dúvidas ou problemas:
1. Verifique os logs no Railway
2. Teste as APIs via `/docs`
3. Confirme as variáveis de ambiente
4. Verifique a documentação da OpenAI

## Licença

Este projeto é fornecido como exemplo educacional. Use e modifique conforme necessário.

