from fastapi import FastAPI
from app.api.whatsapp import router as whatsapp_router
from app.core.config import settings
import logging

app = FastAPI(title=settings.project_name)

logging.basicConfig(level=settings.log_level.upper())

@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "healthy"}

app.include_router(whatsapp_router, prefix="/agente-voz", tags=["WhatsApp Webhook"])
