from datetime import datetime, timedelta
from app.database.connection import db
from app.models.agendamento import agendamento_helper
from bson import ObjectId

collection = db["agendamentos"]

async def listar_agendamentos():
    ags = []
    async for item in collection.find():
        ags.append(agendamento_helper(item))
    return ags

async def criar_agendamento(data: dict):
    conflito = await verificar_conflito(data["data"], data["hora"], data["sala"])
    if conflito:
        return {"erro": "Conflito de agendamento para esta sala e horário."}
    
    res = await collection.insert_one(data)
    return await collection.find_one({"_id": res.inserted_id})

async def atualizar_agendamento(id: str, update_data: dict):
    await collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    return await collection.find_one({"_id": ObjectId(id)})

async def deletar_agendamento(id: str):
    await collection.delete_one({"_id": ObjectId(id)})


def parse_datetime(data_str: str, hora_str: str) -> datetime:
    return datetime.strptime(f"{data_str} {hora_str}", "%Y-%m-%d %H:%M")

async def verificar_conflito(data: str, hora: str, sala: str):
    novo_inicio = parse_datetime(data, hora)
    novo_fim = novo_inicio + timedelta(hours=2)  # ajustar conforme duração real

    async for ag in collection.find({"data": data, "sala": sala}):
        ag_inicio = parse_datetime(ag["data"], ag["hora"])
        ag_fim = ag_inicio + timedelta(hours=2)  # mesmo ajuste

        # Verifica sobreposição
        if (ag_inicio < novo_fim) and (novo_inicio < ag_fim):
            return True
    return False
