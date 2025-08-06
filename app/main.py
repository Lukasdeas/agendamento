from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routers

app = FastAPI(title="Sistema de Agendamento de Cirurgias")

# Configuração do CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",  # Para desenvolvimento local com Live Server
    "frontend-git-main-lucas-souzas-projects-7b26a051.vercel.app",  # URL do seu frontend em produção
    # Adicione outras URLs de frontend se necessário
    "null"  # Para requisições de arquivos locais (file://) em alguns navegadores
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agendamento.router)

@app.get("/")
def root():
    return {"mensagem": "API de Agendamento de Cirurgias funcionando!"}
