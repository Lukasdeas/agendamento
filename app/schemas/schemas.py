from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, time

class AgendamentoBase(BaseModel):
    data: date
    hora: time
    sala: str
    medico: str
    paciente: str
    convenio: str
    status: str

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoUpdate(BaseModel):
    status: Optional[str] = None
    data: Optional[str] = None
    hora: Optional[str] = None

class AgendamentoInDB(AgendamentoBase):
    id: str
