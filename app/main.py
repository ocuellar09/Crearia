from fastapi import FastAPI
from app.api.endpoints import router
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse

app = FastAPI(title="Agente de Voz")

@app.get("/health", include_in_schema=False)
def health_check():
    return HTMLResponse(content="OK")

main_router = APIRouter()
main_router.include_router(router, prefix="/agente-voz")

app.include_router(main_router)