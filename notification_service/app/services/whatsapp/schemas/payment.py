from decimal import Decimal
from .base import BaseWhatsAppRequest

class PaymentSuccessRequest(BaseWhatsAppRequest):
    """
    Schema for payment success notification
    """
    
    customer_name: str
    payment_id: str
    invoice_number: str
    invoice_url: str
    amount: Decimal
    currency: str = "INR"
    