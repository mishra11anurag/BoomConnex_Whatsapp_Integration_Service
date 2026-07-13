from app.services.whatsapp.constants import TEMPLATE
from app.services.whatsapp.registry.template_registry import (
    PAYMENT_SUCCESS_TEMPLATE,
    TEMPLATES,
)
from app.services.whatsapp.schemas.meta_payload import (
    Component,
    Document,
    Language,
    MetaTemplatePayload,
    Parameter,
    Template,
)
from app.services.whatsapp.schemas.payment import PaymentSuccessRequest


def build_payment_template(
    request: PaymentSuccessRequest,
    invoice_number: str,
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
            components=[
                # Document Header
                Component(
                    type="header",
                    parameters=[
                        Parameter(
                            type="text",
                            text = request.customer_name,
                        ),
                    ],
                ),

                # Body
                Component(
                    type="body",
                    parameters=[
                        Parameter(
                            type="text",
                            text=str(request.amount),
                        ),
                        Parameter(
                            type="text",
                            text=request.payment_id,
                        ),
                        Parameter(
                            type="text",
                            text=invoice_number,
                        ),
                    ],
                ),

                # Dynamic URL Button
                Component(
                    type="button",
                    sub_type="url",
                    index="0",
                    parameters=[
                        Parameter(
                            type="text",
                            text=invoice_number,
                        ),
                    ],
                ),
            ],
        ),
    )