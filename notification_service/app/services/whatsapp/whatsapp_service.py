from sqlalchemy.orm import Session

from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.whatsapp.builders.payment_payload import (
    build_payment_template,
)
from app.services.whatsapp.client.meta_client import MetaWhatsAppClient
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest
from app.services.whatsapp.schemas.responses import MetaResponse
from app.models.whatsapp_log import WhatsAppMessageLog
from app.services.invoice.invoice_number_generator import InvoiceNumberGenerator
from pydantic import Field


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
        invoice_number = str(InvoiceNumberGenerator.generate())
        
        payload = build_payment_template(request, invoice_number)
        
        log = WhatsAppMessageLog(
            amount=request.amount,
            invoice_number=invoice_number,
            customer_name=request.customer_name,
            name_of_sme=request.name_of_sme,
            tenant_id=request.tenant_id,
            sme_user_id=request.sme_user_id,
            phone_number=request.phone_number,
            payment_id=request.payment_id,
            meta_message_id="",
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