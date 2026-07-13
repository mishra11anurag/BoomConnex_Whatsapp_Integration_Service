from datetime import datetime


class InvoiceNumberGenerator:
    """
    Generates unique invoice numbers.
    """

    @staticmethod
    def generate() -> str:

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        return f"INV-{timestamp}"