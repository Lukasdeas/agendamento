from fastapi import FastAPI
from app.routers import agendamento

app = FastAPI(title="Sistema de Agendamento de Cirurgias")

app.include_router(agendamento.router)

@app.get("/")
def root():
    return {"mensagem": "API de Agendamento de Cirurgias funcionando!"}
