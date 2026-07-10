from sqlalchemy.orm import Session

from app.models.whatsapp_log import WhatsAppMessageLog


class WhatsAppRepository:

    def __init__(self, db: Session):
        self.db = db

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
    
    def get_all(self):
        return self.db.query(WhatsAppMessageLog).order_by(WhatsAppMessageLog.created_at.desc()).all()
    
    def delete(self, log: WhatsAppMessageLog):
        self.db.delete(log)
        self.db.commit()