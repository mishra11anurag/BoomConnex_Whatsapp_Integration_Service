from pydantic import BaseModel


class Language(BaseModel):
    code: str


class Parameter(BaseModel):
    type: str
    text: str


class Component(BaseModel):
    type: str
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