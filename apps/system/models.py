from django.db import models
from .tasks import generate_notification_async
from django.utils.translation import ugettext_lazy as _

PRODUCT_REQUEST = 1

ACTIONS = (
    (PRODUCT_REQUEST, _('Solicitud de producto')),
)
