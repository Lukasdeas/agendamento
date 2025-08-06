from fastapi import APIRouter
from app.schemas.agendamento import AgendamentoCreate, AgendamentoUpdate
from app.services import agendamento as service

router = APIRouter(prefix="/agendamento", tags=["Agendamentos"])

@router.get("/")
async def listar():
    return await service.listar_agendamentos()

@router.post("/")
async def criar(ag: AgendamentoCreate):
    novo = await service.criar_agendamento(ag.dict())
    return novo

@router.put("/{id}")
async def atualizar(id: str, update: AgendamentoUpdate):
    atualizado = await service.atualizar_agendamento(id, update.dict(exclude_unset=True))
    return atualizado

@router.delete("/{id}")
async def deletar(id: str):
    await service.deletar_agendamento(id)
    return {"msg": "Agendamento excluído"}
