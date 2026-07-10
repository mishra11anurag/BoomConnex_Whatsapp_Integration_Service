import logging

from fastapi import APIRouter, Depends, Request
from fastapi.responses import PlainTextResponse, Response
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.services.whatsapp.schemas.webhook import WebhookPayload
from app.services.whatsapp.webhook_service import WebhookService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"],
)


@router.get("")
async def verify_webhook(request: Request) -> Response:
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == settings.whatsapp_verify_token:
        logger.info("Webhook verified successfully")
        return PlainTextResponse(content=challenge, status_code=200)

    logger.warning(
        "Webhook verification failed: mode=%s, token=%s",
        mode,
        token,
    )
    return PlainTextResponse(
        content="Verification failed",
        status_code=403,
    )


@router.post("")
async def receive_webhook(
    payload: WebhookPayload,
    db: Session = Depends(get_db),
) -> Response:
    logger.info(
        "Received webhook event: object=%s, entries=%d",
        payload.object,
        len(payload.entry),
    )

    try:
        service = WebhookService(db)
        service.process(payload)
    except Exception:
        logger.exception("Failed to process webhook event")

    return Response(status_code=200)
