    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from app.routers import agendamento

    app = FastAPI(title="Sistema de Agendamento de Cirurgias")

    # Configuração do CORS
    origins = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:5500", # Se você estiver testando localmente com Live Server
        "https://frontend-sepia-kappa-28.vercel.app/",
        # Exemplo: "https://seu-frontend.github.io",
        # Exemplo: "https://seu-frontend.netlify.app",
        "null" # Pode ser necessário para requisições de arquivos locais (file://) em alguns navegadores
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
    
