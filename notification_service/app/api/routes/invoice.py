from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.invoice.invoice_service import InvoiceService

router = APIRouter(
    prefix="/invoice",
    tags=["Invoice"],
)


@router.get("/{invoice_number}")
def get_invoice(
    invoice_number: str,
    db: Session = Depends(get_db),
):
    repository = WhatsAppRepository(db)
    service = InvoiceService(repository)

    try:
        pdf = service.generate_invoice(invoice_number)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found.",
        )

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'inline; filename="{invoice_number}.pdf"'
        },
    )