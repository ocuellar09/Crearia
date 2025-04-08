from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Agente de voz en funcionamiento 🎤"}

@router.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy"}

