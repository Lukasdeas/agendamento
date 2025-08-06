def agendamento_helper(agendamento) -> dict:
    return {
        "id": str(agendamento["_id"]),
        "data": agendamento["data"],
        "hora": agendamento["hora"],
        "sala": agendamento["sala"],
        "medico": agendamento["medico"],
        "paciente": agendamento["paciente"],
        "convenio": agendamento["convenio"],
        "status": agendamento["status"]
    }
