from typing import Optional

from pydantic import BaseModel


class WebhookMetadata(BaseModel):
    display_phone_number: str
    phone_number_id: str


class Profile(BaseModel):
    name: str


class TextContent(BaseModel):
    body: str


class AudioContent(BaseModel):
    id: str
    mime_type: str


class DocumentContent(BaseModel):
    id: str
    mime_type: str
    filename: Optional[str] = None


class ImageContent(BaseModel):
    id: str
    mime_type: str


class VideoContent(BaseModel):
    id: str
    mime_type: str


class Message(BaseModel):
    from_: str
    id: str
    timestamp: str
    type: Optional[str] = None
    text: Optional[TextContent] = None
    audio: Optional[AudioContent] = None
    document: Optional[DocumentContent] = None
    image: Optional[ImageContent] = None
    video: Optional[VideoContent] = None


class StatusPricing(BaseModel):
    billable: bool
    pricing_model: str
    category: str


class ConversationOrigin(BaseModel):
    type: str


class Conversation(BaseModel):
    id: str
    origin: ConversationOrigin
    expiration_timestamp: Optional[str] = None


class Status(BaseModel):
    id: str
    recipient_id: str
    status: str
    timestamp: str
    type: Optional[str] = None
    pricing: Optional[StatusPricing] = None
    conversation: Optional[Conversation] = None


class ChangeValue(BaseModel):
    messaging_product: str
    metadata: WebhookMetadata
    contacts: Optional[list[Profile]] = None
    messages: Optional[list[Message]] = None
    statuses: Optional[list[Status]] = None


class Change(BaseModel):
    field: str
    value: ChangeValue


class Entry(BaseModel):
    id: str
    changes: list[Change]


class WebhookPayload(BaseModel):
    object: str
    entry: list[Entry]
