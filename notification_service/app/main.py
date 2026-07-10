import logging

from fastapi import FastAPI

from app.api.routes.whatsapp import router as whatsapp_router
from app.api.routes.webhook import router as webhook_router
from app.db.database import Base, engine
from app.models.whatsapp_log import WhatsAppMessageLog

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(
    title="Notification Service",
    version="1.0.0",
)

app.include_router(whatsapp_router)
app.include_router(webhook_router)


@app.get("/")
def root():
    return {
        "message": "Notification Service is running."
    }