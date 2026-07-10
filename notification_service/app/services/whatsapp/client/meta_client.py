import httpx

from app.core.config import settings
from app.services.whatsapp.constants import (
    GRAPH_API_BASE_URL,
    MESSAGES_ENDPOINT,
    
)
from app.services.whatsapp.schemas.meta_payload import MetaTemplatePayload
from app.services.whatsapp.schemas.responses import MetaResponse

class MetaWhatsAppClient:
    """
     Client for communicating with Meta WhatsApp Cloud API.
    """
    def __init__(self):
        self.base_url = (
            f"{GRAPH_API_BASE_URL}/"
            f"{settings.whatsapp_api_version}/"
            f"{settings.whatsapp_phone_number_id}/"
            f"{MESSAGES_ENDPOINT}"
            
        )
        self.headers = {
            "Authorization": f"Bearer {settings.whatsapp_access_token}",
            "Content-Type": "application/json",
        }
        self.client = httpx.AsyncClient(timeout=30)
        
        
    async def send_template_message(
        self,
        payload: MetaTemplatePayload,
    ) -> MetaResponse:
        """
        Send a template message to Meta WhatsApp Cloud API.
        """

        response = await self.client.post(
            url=self.base_url,
            headers=self.headers,
            json=payload.model_dump(),
        )
        print("URL:", self.base_url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        response.raise_for_status()

        return MetaResponse(**response.json())

    async def close(self):
        """
        Close the HTTP client.
        """

        await self.client.aclose()