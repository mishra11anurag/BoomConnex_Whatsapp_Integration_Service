from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest
from app.services.whatsapp.whatsapp_service import WhatsAppService

router = APIRouter(
    prefix="/whatsapp",
    tags=["WhatsApp"],
)

@router.post("/payment-success")
async def send_payment_success(
    request: PaymentSuccessRequest,
    db: Session = Depends(get_db),
):

    service = WhatsAppService(db)

    return await service.send_payment_success(request)