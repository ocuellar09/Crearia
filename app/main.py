from fastapi import FastAPI, Request
from app.api.endpoints import router
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

app = FastAPI(title="Agente de Voz")

# Añadir el health check directamente a la aplicación principal
@app.api_route("/health", methods=["GET", "HEAD"], include_in_schema=False)
async def health_check(request: Request):
    return JSONResponse(content={"status": "healthy"})

main_router = APIRouter()
main_router.include_router(router, prefix="/agente-voz")

app.include_router(main_router)