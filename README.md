# 🚀 Template FastAPI + Vue.js

Template completo para aplicações full-stack com **FastAPI** (backend) e **Vue.js** (frontend), utilizando arquitetura DDD e MongoDB com Beanie ODM.

## 📁 Estrutura do Projeto

```
projeto/
├── app/                          # Backend FastAPI (DDD)
│   ├── api/                      # Camada de API
│   │   ├── routers/             # Routers/Controllers
│   │   │   ├── __init__.py
│   │   │   └── cadastro.py
│   │   └── dependencies.py
│   ├── repositories/            # Camada de Dados
│   │   └── cadastro_repository.py
│   ├── infra/                   # Infraestrutura
│   │   ├── mongo/
│   │   │   └── config.py       # Configuração MongoDB
│   │   └── schemas/
│   │       └── cadastro.py     # Models Beanie
│   ├── dist/                    # Build do Vue.js (gerado)
│   └── main.py                  # Entrypoint FastAPI
├── frontend/                     # Frontend Vue.js
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
├── .env                         # Variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologias

### Backend
- **FastAPI** - Framework web moderno e rápido
- **Beanie** - ODM async para MongoDB (equivalente ao Mongoose)
- **Motor** - Driver async do MongoDB
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

### Frontend
- **Vue.js 3** - Framework progressivo
- **Vite** - Build tool rápido
- **Vue Router** - Roteamento SPA

### Banco de Dados
- **MongoDB Atlas** - Banco de dados NoSQL na nuvem

## 🚀 Setup e Instalação

### 0. Comandos básicos
- Criar ambiente virtual

python -m venv .venv

- Ativar (Linux/Mac)

source venv/bin/activate

- Ativar (Windows)

venv\Scripts\activate

- Instalar dependências

pip install -r requirements.txt

- Atualizar requirements.txt

pip install <lib>

pip freeze > requirements.txt


### 1. Clonar o repositório

```bash
git clone <seu-repositorio>
cd <nome-do-projeto>
```

### 2. Configurar Backend

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_KEY=mongodb+srv://usuario:<senha>@cluster.mongodb.net/nome_do_banco
```

### 4. Configurar Frontend

```bash
cd frontend
npm install
```

## 🎯 Como Usar

### Desenvolvimento

#### Rodar Backend (FastAPI)
```bash
# Na raiz do projeto
uvicorn app.main:app --reload
```

O backend estará disponível em: `http://localhost:8000`
- API Docs (Swagger): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

#### Rodar Frontend (Vue.js)
```bash
cd frontend
npm run dev
```

O frontend estará disponível em: `http://localhost:5173`

---

### Produção

#### 1. Build do Frontend
```bash
cd frontend
npm run build
```

Este comando gera a pasta `dist` dentro de `app/`, que será servida pelo FastAPI.

#### 2. Rodar aplicação completa
```bash
# Na raiz do projeto
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Agora o FastAPI serve tanto a API quanto o frontend:
- Frontend: `http://localhost:8000/`
- API: `http://localhost:8000/api/`
- Docs: `http://localhost:8000/docs`

## 📝 Configuração do Build

### vite.config.js

Configure o Vite para gerar o build dentro da pasta `app`:

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: '../app/dist',  // Build vai para app/dist
    emptyOutDir: true
  }
})
```

### package.json

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

## 🔌 Endpoints da API

### Cadastro

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/cadastro/` | Lista todos os cadastros (paginado) |
| `GET` | `/api/cadastro/{id}` | Busca cadastro por ID |
| `GET` | `/api/cadastro/search/?q=termo` | Busca cadastros por nome |
| `POST` | `/api/cadastro/` | Cria novo cadastro |
| `PUT` | `/api/cadastro/{id}` | Atualiza cadastro completo |
| `PATCH` | `/api/cadastro/{id}` | Atualiza cadastro parcial |
| `DELETE` | `/api/cadastro/{id}` | Deleta cadastro |
| `GET` | `/api/cadastro/count/total` | Conta total de cadastros |

### Exemplo de Request

```bash
# Criar cadastro
curl -X POST "http://localhost:8000/api/cadastro/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "senha": "senha123",
    "floatLis": ["1.5", "2.3"]
  }'
```

## 🏗️ Arquitetura DDD

```
app/
├── api/              # Presentation Layer (Controllers/Routers)
├── repositories/     # Data Access Layer
├── infra/           # Infrastructure (DB, External Services)
└── main.py          # Application Entry Point
```

### Benefícios:
- ✅ Separação de responsabilidades
- ✅ Código testável e manutenível
- ✅ Fácil de escalar
- ✅ Independência de frameworks

## 📦 Dependências

### requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
motor==3.3.2
beanie==1.23.6
pydantic==2.5.0
python-dotenv==1.0.0
```

### Instalar:
```bash
pip install -r requirements.txt
```

## 🔒 Boas Práticas

### .gitignore

```gitignore
# Python
.venv
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment
.env
.env.local

# Frontend
node_modules/
frontend/dist/

# Build do Vue no FastAPI
app/dist/

# IDE
.vscode/
.idea/

# Logs
*.log
```

## 🌐 Deploy

### Opções de Deploy:

1. **Railway** - Deploy automático via Git
2. **Render** - Free tier com MongoDB Atlas
3. **Heroku** - Plataforma tradicional
4. **DigitalOcean** - VPS com Docker
5. **AWS/GCP/Azure** - Cloud providers

### Dockerfile exemplo:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido com ❤️ usando FastAPI e Vue.js

---

## 📚 Recursos Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Vue.js](https://vuejs.org/)
- [Documentação Beanie](https://beanie-odm.dev/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Pydantic](https://docs.pydantic.dev/)