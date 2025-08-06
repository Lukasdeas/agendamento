from pydantic import BaseModel
from typing import Optional

class AgendamentoBase(BaseModel):
    data: str
    hora: str
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
