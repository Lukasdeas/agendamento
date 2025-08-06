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
    res = await collection.insert_one(data)
    return await collection.find_one({"_id": res.inserted_id})

async def atualizar_agendamento(id: str, update_data: dict):
    await collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    return await collection.find_one({"_id": ObjectId(id)})

async def deletar_agendamento(id: str):
    await collection.delete_one({"_id": ObjectId(id)})
