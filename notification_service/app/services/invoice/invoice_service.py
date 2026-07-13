from pathlib import Path

from app.repositories.whatsapp_repository import WhatsAppRepository
from app.services.invoice.pdf_service import PDFService
from app.services.invoice.template_engine import TemplateEngine


class InvoiceService:
    """
    Service responsible for generating invoices.
    """

    def __init__(
        self,
        repository: WhatsAppRepository,
    ):

        template_dir = Path(__file__).parent / "templates"

        self.repository = repository
        self.template_engine = TemplateEngine(template_dir)
        self.pdf_service = PDFService()

    def generate_invoice(
        self,
        invoice_number: str,
    ):
        """
        Generate invoice PDF from invoice number.
        """

        log = self.repository.get_by_invoice_number(invoice_number)

        if not log:
            raise ValueError("Invoice not found.")

        html = self.template_engine.render(
            template_name="payment_success.html",
            context={
                "customer_name": log.customer_name,
                "name_of_sme": log.name_of_sme,
                "payment_id": log.payment_id,
                "invoice_number": log.invoice_number,
                "invoice_date": log.created_at.strftime("%d %b %Y"),
                "amount": log.amount,
            },
        )

        pdf = self.pdf_service.generate(
            html_content=html,
        )

        return pdf