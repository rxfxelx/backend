# Instruções de Deploy no Vercel

## Pré-requisitos

1. **Conta no Vercel:** Crie uma conta gratuita em [vercel.com](https://vercel.com)
2. **Chave da OpenAI:** Obtenha em [platform.openai.com](https://platform.openai.com/api-keys)
3. **Vercel CLI (opcional):** Para deploy via linha de comando

## Método 1: Deploy via Interface Web (Recomendado)

### Passo 1: Preparar o Repositório
1. Crie um repositório no GitHub
2. Faça upload de todos os arquivos do projeto
3. Certifique-se que a estrutura está correta:
   ```
   seu-repositorio/
   ├── api/
   │   ├── index.py
   │   ├── models.py
   │   ├── database.py
   │   └── ai_service.py
   ├── requirements.txt
   ├── vercel.json
   └── README.md
   ```

### Passo 2: Conectar ao Vercel
1. Acesse [vercel.com](https://vercel.com) e faça login
2. Clique em "New Project"
3. Conecte sua conta do GitHub
4. Selecione o repositório do projeto
5. Clique em "Import"

### Passo 3: Configurar Variáveis de Ambiente
1. Na página do projeto, vá em "Settings"
2. Clique em "Environment Variables"
3. Adicione a variável:
   - **Name:** `OPENAI_API_KEY`
   - **Value:** Sua chave da API da OpenAI
   - **Environment:** Production (e Development se quiser testar)
4. Clique em "Save"

### Passo 4: Deploy
1. Clique em "Deploy" ou aguarde o deploy automático
2. Aguarde o processo de build e deploy
3. Sua API estará disponível em: `https://seu-projeto.vercel.app`

## Método 2: Deploy via CLI

### Passo 1: Instalar Vercel CLI
```bash
npm i -g vercel
```

### Passo 2: Login
```bash
vercel login
```

### Passo 3: Deploy
```bash
# No diretório do projeto
vercel

# Siga as instruções:
# - Set up and deploy? Y
# - Which scope? (sua conta)
# - Link to existing project? N
# - What's your project's name? ia-vendedora
# - In which directory is your code located? ./
```

### Passo 4: Configurar Variável de Ambiente
```bash
vercel env add OPENAI_API_KEY
# Cole sua chave da OpenAI quando solicitado
# Selecione Production (e Development se quiser)
```

### Passo 5: Redeploy com as Variáveis
```bash
vercel --prod
```

## Testando o Deploy

### 1. Verificar Status da API
Acesse: `https://seu-projeto.vercel.app/api/health`

Resposta esperada:
```json
{
  "status": "ok",
  "message": "IA Vendedora API está funcionando"
}
```

### 2. Acessar Documentação
Acesse: `https://seu-projeto.vercel.app/docs`

### 3. Testar APIs Básicas
```bash
# Listar produtos (deve retornar array vazio inicialmente)
curl https://seu-projeto.vercel.app/api/products

# Verificar estatísticas
curl https://seu-projeto.vercel.app/api/stats
```

## Configuração do Frontend

Após o deploy do backend, use a URL do Vercel no prompt do frontend:

```javascript
// Substitua esta URL no código do frontend
const API_BASE_URL = 'https://seu-projeto.vercel.app/api';
```

## Solução de Problemas

### Erro de Build
- Verifique se `requirements.txt` está correto
- Confirme que `vercel.json` está na raiz do projeto
- Verifique logs de build no dashboard do Vercel

### Erro 500 na API
- Verifique se `OPENAI_API_KEY` está configurada
- Veja os logs de função no dashboard do Vercel
- Teste localmente primeiro

### Erro de CORS
- O CORS já está configurado para aceitar qualquer origem
- Se necessário, ajuste em `api/index.py`

### Banco de Dados
- SQLite funciona no Vercel mas é efêmero
- Para produção, considere PostgreSQL ou MongoDB
- Dados podem ser perdidos entre deploys

## Próximos Passos

1. **Gerar Frontend:** Use o `PROMPT_FRONTEND.md` numa IA
2. **Deploy Frontend:** Pode ser no mesmo projeto Vercel
3. **Configurar Domínio:** Opcional, nas configurações do projeto
4. **Monitoramento:** Use o dashboard do Vercel para logs e métricas

## URLs Importantes

- **API Base:** `https://seu-projeto.vercel.app/api`
- **Documentação:** `https://seu-projeto.vercel.app/docs`
- **Health Check:** `https://seu-projeto.vercel.app/api/health`
- **Dashboard Vercel:** [vercel.com/dashboard](https://vercel.com/dashboard)

## Limitações do Plano Gratuito

- **Execuções:** 100GB-hours por mês
- **Bandwidth:** 100GB por mês
- **Funções:** 10 segundos de timeout
- **Projetos:** Ilimitados

Para a maioria dos casos de uso, o plano gratuito é suficiente.

