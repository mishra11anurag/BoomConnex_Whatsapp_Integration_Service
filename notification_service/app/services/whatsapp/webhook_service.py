import logging

from sqlalchemy.orm import Session

from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.whatsapp.schemas.webhook import WebhookPayload

logger = logging.getLogger(__name__)


class WebhookService:

    def __init__(self, db: Session):
        self.repository = WhatsAppRepository(db)

    def process(self, payload: WebhookPayload) -> None:
        for entry in payload.entry:
            for change in entry.changes:
                if change.field != "messages":
                    continue

                value = change.value

                if value.statuses:
                    self._handle_statuses(value.statuses)

                if value.messages:
                    self._handle_messages(value.messages)

    def _handle_statuses(self, statuses: list) -> None:
        for status in statuses:
            log = self.repository.get_by_meta_message_id(status.id)
            if log is None:
                logger.warning("No log found for message %s", status.id)
                continue

            log.status = status.status.upper()
            self.repository.update(log)
            logger.info(
                "Updated message %s status to %s",
                status.id,
                status.status,
            )

    def _handle_messages(self, messages: list) -> None:
        for msg in messages:
            logger.info(
                "Received incoming message %s from %s",
                msg.id,
                msg.from_,
            )
