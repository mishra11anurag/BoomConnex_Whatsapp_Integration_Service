class WhatsAppException(Exception):
    """
    Base exception for WhatsApp module.
    """
    pass


class MetaAPIException(WhatsAppException):
    """
    Raised when Meta API returns an error.
    """
    pass


class TemplateNotFoundException(WhatsAppException):
    """
    Raised when the requested WhatsApp template is not found.
    """
    pass


class MediaUploadException(WhatsAppException):
    """
    Raised when media upload fails.
    """
    pass