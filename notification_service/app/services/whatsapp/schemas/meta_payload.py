from pydantic import BaseModel


class Language(BaseModel):
    code: str

class Document(BaseModel):
    link: str
    filename: str

class Parameter(BaseModel):
    type: str
    text: str | None = None
    document: Document | None = None

class Component(BaseModel):
    type: str
    sub_type: str | None = None
    index: str | None = None
    parameters: list[Parameter]


class Template(BaseModel):
    name: str
    language: Language
    components: list[Component] | None = None


class MetaTemplatePayload(BaseModel):
    messaging_product: str
    to: str
    type: str
    template: Template

