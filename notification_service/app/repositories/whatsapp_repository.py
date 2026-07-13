from sqlalchemy.orm import Session

from app.models.whatsapp_log import WhatsAppMessageLog


class WhatsAppRepository:

    def __init__(self, db: Session):
        self.db = db
    # This repository is responsible for handling the database operations related to WhatsAppMessageLog model.
    # CRUD operations are implemented here to interact with the database.
    def save(self, log: WhatsAppMessageLog):

        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)

        return log

    def update(self, log: WhatsAppMessageLog):

        self.db.commit()
        self.db.refresh(log)

        return log

    def get_by_id(self, log_id):

        return (
            self.db.query(WhatsAppMessageLog)
            .filter(WhatsAppMessageLog.id == log_id)
            .first()
        )

    def get_by_meta_message_id(self, meta_message_id: str):
        return (
            self.db.query(WhatsAppMessageLog)
            .filter(WhatsAppMessageLog.meta_message_id == meta_message_id)
            .first()
        )
    
    def get_by_invoice_number(
    self,
    invoice_number: str,
    ):
        return (
            self.db.query(WhatsAppMessageLog)
            .filter(
                WhatsAppMessageLog.invoice_number == invoice_number
            )
            .first()
        )
    
    def get_all(self):
        return self.db.query(WhatsAppMessageLog).order_by(WhatsAppMessageLog.created_at.desc()).all()
    
    def delete(self, log: WhatsAppMessageLog):
        self.db.delete(log)
        self.db.commit()