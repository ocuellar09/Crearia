from fastapi import APIRouter, Request
from fastapi.responses import Response
import logging

router = APIRouter()
logger = logging.getLogger("whatsapp")

@router.get("/")
async def root():
    return {"message": "Agente de voz en funcionamiento 🎤"}

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    from_number = form.get("From")
    message_body = form.get("Body")

    logger.info(f"📩 Mensaje recibido de {from_number}: {message_body}")

    respuesta = f"<Response><Message>Hola 👋, recibimos tu mensaje: {message_body}</Message></Response>"
    return Response(content=respuesta, media_type="application/xml")
