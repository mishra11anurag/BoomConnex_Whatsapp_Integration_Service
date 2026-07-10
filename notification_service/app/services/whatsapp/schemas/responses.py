from pydantic import BaseModel


class Contact(BaseModel):
    input: str
    wa_id: str


class Message(BaseModel):
    id: str


class MetaResponse(BaseModel):
    messaging_product: str
    contacts: list[Contact]
    messages: list[Message]