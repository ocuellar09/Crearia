from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Agente de voz en funcionamiento 🎤"}

# Eliminamos este endpoint ya que ahora está en main.py
# @router.api_route("/health", methods=["GET", "HEAD"], include_in_schema=False)
# async def health_check(request: Request):
#     return JSONResponse(content={"status": "healthy"})