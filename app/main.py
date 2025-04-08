from fastapi import FastAPI
from app.api.endpoints import router
from fastapi.routing import APIRouter

app = FastAPI(title="Agente de Voz")

main_router = APIRouter()
main_router.include_router(router, prefix="/agente-voz")

app.include_router(main_router)
