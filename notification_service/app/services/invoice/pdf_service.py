from io import BytesIO

from xhtml2pdf import pisa


class PDFService:
    """
    Service for generating PDF from rendered HTML.
    """

    def generate(
        self,
        html_content: str,
    ) -> BytesIO:
        """
        Generate PDF from HTML and return it as BytesIO.
        """

        pdf_buffer = BytesIO()

        pisa_status = pisa.CreatePDF(
            src=html_content,
            dest=pdf_buffer,
        )

        if pisa_status.err:
            raise Exception("Failed to generate PDF.")

        pdf_buffer.seek(0)

        return pdf_buffer