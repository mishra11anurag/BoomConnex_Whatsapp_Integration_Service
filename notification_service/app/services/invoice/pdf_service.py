from pathlib import Path

from weasyprint import HTML


class PDFService:
    """
    Service for generating PDF files from HTML.
    """

    def generate(
        self,
        html_content: str,
        output_path: str,
    ) -> str:
        """
        Generate a PDF from rendered HTML.
        """

        output_file = Path(output_path)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        HTML(
            string=html_content,
        ).write_pdf(
            target=str(output_file),
        )

        return str(output_file)