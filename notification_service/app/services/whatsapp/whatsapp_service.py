from sqlalchemy.orm import Session

from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.whatsapp.builders.payment_payload import (
    build_payment_template,
)
from app.services.whatsapp.client.meta_client import MetaWhatsAppClient
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest
from app.services.whatsapp.schemas.responses import MetaResponse
from app.models.whatsapp_log import WhatsAppMessageLog

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
        
        log = WhatsAppMessageLog(
            name_of_sme=request.name_of_sme,
            tenant_id=request.tenant_id,
            sme_user_id=request.sme_user_id,
            phone_number=request.phone_number,
            payment_id=request.payment_id,
            status="pending",
        )
        self.repository.save(log)

        response = await self.client.send_template_message(
            payload
        )
        
        log.meta_message_id = response.messages[0].id
        log.status = "sent"
        self.repository.update(log)

        return response

    async def close(self):
        """
        Close the WhatsApp client.
        """

        await self.client.close()