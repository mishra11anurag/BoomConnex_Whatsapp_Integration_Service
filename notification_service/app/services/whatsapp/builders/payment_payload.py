from app.services.whatsapp.constants import TEMPLATE
from app.services.whatsapp.registry.template_registry import (
    PAYMENT_SUCCESS_TEMPLATE,
    TEMPLATES,
)
from app.services.whatsapp.schemas.meta_payload import (
    Language,
    MetaTemplatePayload,
    Template,
)
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest


def build_payment_template(
    request: PaymentSuccessRequest,
) -> MetaTemplatePayload:

    template = TEMPLATES[PAYMENT_SUCCESS_TEMPLATE]

    return MetaTemplatePayload(
    messaging_product="whatsapp",
    to=request.phone_number,
    type=TEMPLATE,
    template=Template(
        name=template["name"],
        language=Language(
            code=template["language"],
        ),
    ),
)