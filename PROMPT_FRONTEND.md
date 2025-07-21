# Prompt para IA de Frontend - Sistema de IA Vendedora

## Contexto do Projeto

Você deve criar um painel de administração web moderno e responsivo para um sistema de IA vendedora. O backend já está pronto e funcionando com FastAPI, hospedado no Vercel. Sua tarefa é criar um frontend completo que se conecte com as APIs do backend.

## Tecnologias Requeridas

- **HTML5, CSS3, JavaScript (Vanilla ou React)**
- **Design responsivo (mobile-first)**
- **Interface moderna e intuitiva**
- **Integração com APIs REST**

## Estrutura do Sistema

O sistema possui três funcionalidades principais:
1. **Gerenciamento de Produtos** - CRUD completo de produtos
2. **Configuração da IA** - Personalização do comportamento da vendedora virtual
3. **Chat com a IA** - Interface para testar e interagir com a IA vendedora

## APIs Disponíveis

### Base URL
```
https://<SUA_URL_RAILWAY>.up.railway.app/api
```

### 1. APIs de Produtos

#### GET /api/products
**Descrição:** Lista todos os produtos
**Resposta:**
```json
[
  {
    "id": 1,
    "name": "Produto Exemplo",
    "description": "Descrição do produto",
    "price": 99.99,
    "category": "Categoria",
    "stock": 10,
    "image_url": "https://exemplo.com/imagem.jpg",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
]
```

#### GET /api/products/{id}
**Descrição:** Busca um produto específico
**Resposta:** Objeto produto individual

#### POST /api/products
**Descrição:** Cria um novo produto
**Body:**
```json
{
  "name": "Nome do Produto",
  "description": "Descrição detalhada",
  "price": 99.99,
  "category": "Categoria",
  "stock": 10,
  "image_url": "https://exemplo.com/imagem.jpg"
}
```

#### PUT /api/products/{id}
**Descrição:** Atualiza um produto existente
**Body:** Campos opcionais para atualização

#### DELETE /api/products/{id}
**Descrição:** Remove um produto

### 2. APIs de Configuração da IA

#### GET /api/ai-config
**Descrição:** Busca a configuração atual da IA
**Resposta:**
```json
{
  "id": 1,
  "name": "Maria Vendedora",
  "personality": "Amigável, profissional e prestativa",
  "greeting_message": "Olá! Sou a Maria, como posso ajudá-lo hoje?",
  "sales_approach": "Consultiva, focando nas necessidades do cliente",
  "tone": "Amigável e profissional",
  "language": "pt-br",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

#### POST /api/ai-config
**Descrição:** Cria/atualiza a configuração da IA
**Body:**
```json
{
  "name": "Nome da IA",
  "personality": "Descrição da personalidade",
  "greeting_message": "Mensagem de saudação",
  "sales_approach": "Abordagem de vendas",
  "tone": "Tom de voz",
  "language": "pt-br"
}
```

### 3. API do Chat

#### POST /api/chat
**Descrição:** Envia mensagem para a IA
**Body:**
```json
{
  "message": "Olá, estou procurando um produto",
  "user_id": "opcional"
}
```
**Resposta:**
```json
{
  "response": "Olá! Fico feliz em ajudá-lo. Que tipo de produto você está procurando?",
  "products_mentioned": []
}
```

### 4. APIs de Informações

#### GET /api/health
**Descrição:** Verifica se a API está funcionando

#### GET /api/stats
**Descrição:** Retorna estatísticas do sistema

## Design e Layout Requerido

### Paleta de Cores
- **Primária:** #2563eb (azul moderno)
- **Secundária:** #10b981 (verde sucesso)
- **Fundo:** #f8fafc (cinza claro)
- **Texto:** #1e293b (cinza escuro)
- **Bordas:** #e2e8f0 (cinza claro)

### Componentes Principais

#### 1. Header/Navbar
- Logo do sistema "IA Vendedora"
- Menu de navegação (Produtos, Configuração IA, Chat, Dashboard)
- Indicador de status da API

#### 2. Sidebar (Desktop)
- Navegação principal
- Estatísticas rápidas
- Status da configuração da IA

#### 3. Dashboard Principal
- Cards com estatísticas (total de produtos, status da IA)
- Gráficos simples (se possível)
- Ações rápidas

#### 4. Página de Produtos
- Tabela/grid de produtos com:
  - Imagem (thumbnail)
  - Nome
  - Categoria
  - Preço
  - Estoque
  - Ações (editar, excluir)
- Botão "Adicionar Produto"
- Filtros por categoria
- Busca por nome

#### 5. Formulário de Produto
- Campos: nome, descrição, preço, categoria, estoque, URL da imagem
- Validação de campos obrigatórios
- Preview da imagem
- Botões salvar/cancelar

#### 6. Página de Configuração da IA
- Formulário com todos os campos de configuração
- Preview da personalidade
- Botão "Testar Configuração"
- Salvar configurações

#### 7. Interface de Chat
- Área de mensagens (histórico)
- Campo de input para nova mensagem
- Botão enviar
- Indicador de "digitando"
- Produtos mencionados destacados

### Funcionalidades Específicas

#### Gerenciamento de Produtos
1. **Listagem:** Exibir produtos em cards ou tabela
2. **Adicionar:** Modal ou página para novo produto
3. **Editar:** Modal ou página para edição
4. **Excluir:** Confirmação antes de excluir
5. **Busca:** Filtro em tempo real
6. **Categorias:** Filtro por categoria

#### Configuração da IA
1. **Formulário completo** com todos os campos
2. **Preview** da configuração em tempo real
3. **Teste** da IA com a nova configuração
4. **Validação** de campos obrigatórios

#### Chat Interface
1. **Histórico** de mensagens
2. **Envio** de mensagens
3. **Produtos mencionados** destacados
4. **Status** da IA (online/offline)

### Responsividade

#### Mobile (< 768px)
- Menu hambúrguer
- Cards empilhados
- Formulários em tela cheia
- Chat otimizado para mobile

#### Tablet (768px - 1024px)
- Sidebar colapsável
- Grid de produtos 2 colunas
- Formulários em modal

#### Desktop (> 1024px)
- Sidebar fixa
- Grid de produtos 3-4 colunas
- Múltiplas colunas no dashboard

## Exemplos de Código

### Função para buscar produtos
```javascript
async function fetchProducts() {
    try {
        const response = await fetch('https://seu-projeto.vercel.app/api/products');
        const products = await response.json();
        return products;
    } catch (error) {
        console.error('Erro ao buscar produtos:', error);
        return [];
    }
}
```

### Função para criar produto
```javascript
async function createProduct(productData) {
    try {
        const response = await fetch('https://seu-projeto.vercel.app/api/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productData)
        });
        return await response.json();
    } catch (error) {
        console.error('Erro ao criar produto:', error);
        throw error;
    }
}
```

### Função para chat
```javascript
async function sendMessage(message) {
    try {
        const response = await fetch('https://seu-projeto.vercel.app/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message })
        });
        return await response.json();
    } catch (error) {
        console.error('Erro no chat:', error);
        throw error;
    }
}
```

## Estrutura de Arquivos Sugerida

```
frontend/
├── index.html
├── css/
│   ├── style.css
│   └── responsive.css
├── js/
│   ├── app.js
│   ├── products.js
│   ├── ai-config.js
│   └── chat.js
├── images/
│   └── logo.png
└── components/
    ├── header.html
    ├── sidebar.html
    └── modals.html
```

## Requisitos Específicos

### Validações
- Campos obrigatórios destacados
- Validação de preço (números positivos)
- Validação de estoque (números inteiros)
- URLs de imagem válidas

### UX/UI
- Loading states durante requisições
- Mensagens de sucesso/erro
- Confirmações para ações destrutivas
- Tooltips explicativos

### Performance
- Lazy loading de imagens
- Debounce na busca
- Cache de dados quando apropriado

## Entregáveis Esperados

1. **Código HTML, CSS e JavaScript** completo e funcional
2. **Design responsivo** testado em diferentes dispositivos
3. **Integração completa** com todas as APIs
4. **Documentação** de como usar o sistema
5. **Instruções** de instalação e configuração

## Observações Importantes

- O backend está configurado com CORS liberado
- Todas as APIs retornam JSON
- Erros são retornados com status HTTP apropriados
- O sistema deve funcionar sem autenticação (para simplicidade)
- Priorize a usabilidade e experiência do usuário
- Mantenha o código limpo e bem comentado

Crie um sistema completo, moderno e profissional que permita gerenciar produtos, configurar a IA e testar o chat de forma intuitiva e eficiente.

