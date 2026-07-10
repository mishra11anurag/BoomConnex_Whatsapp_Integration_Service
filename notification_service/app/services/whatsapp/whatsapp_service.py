from sqlalchemy.orm import Session

from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.whatsapp.builders.payment_payload import (
    build_payment_template,
)
from app.services.whatsapp.client.meta_client import MetaWhatsAppClient
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest
from app.services.whatsapp.schemas.responses import MetaResponse

class WhatsAppService:
    """
    Service responsible for sending WhatsApp notifications.
    """

    def __init__(self, db:Session):
        self.client = MetaWhatsAppClient()
        self.repository = WhatsAppRepository(db)

    async def send_payment_success(
        self,
        request: PaymentSuccessRequest,
    ) -> MetaResponse:
        """
        Send payment success notification.
        """

        payload = build_payment_template(request)

        response = await self.client.send_template_message(
            payload
        )

        return response

    async def close(self):
        """
        Close the WhatsApp client.
        """

        await self.client.close()