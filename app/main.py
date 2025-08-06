from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routers

app = FastAPI(title="Sistema de Agendamento de Cirurgias")

# Configuração do CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "https://frontend-de-produção.vercel.app"
    # não inclua "null" ou "*" se usar credentials
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
