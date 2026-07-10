from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class WhatsAppMessageLog(Base):
    
    __tablename__ = "whatsapp_message_logs"

    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    tenant_id = Column(UUID(as_uuid=True),nullable=False)
    sme_user_id = Column(UUID(as_uuid=True),nullable=False)
    phone_number = Column(String(20),nullable=False)
    payment_id = Column(String(100),nullable=False)
    meta_message_id = Column(String(255),nullable=True)
    status = Column(String(20),nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)