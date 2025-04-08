from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Agente de Voz")

app.include_router(router)
