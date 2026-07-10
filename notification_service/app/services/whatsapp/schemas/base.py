from uuid import UUID
from pydantic import BaseModel

class BaseWhatsAppRequest(BaseModel):
    # Base Schema for all whatsapp notifications
    
    tenant_id: UUID
    sme_user_id: UUID
    phone_number: str
    