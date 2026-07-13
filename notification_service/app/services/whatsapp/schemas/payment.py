from decimal import Decimal
from .base import BaseWhatsAppRequest
from datetime import datetime




class PaymentSuccessRequest(BaseWhatsAppRequest):
    """
    Schema for payment success notification
    """
    customer_name: str
    name_of_sme: str
    payment_id: str
    amount: Decimal
    invoice_number: str = ""
    currency: str = "INR"
    created_at: datetime = datetime.now()