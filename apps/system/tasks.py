from fcm_django.models import FCMDevice

from apps.system.models import PRODUCT_REQUEST


def generate_notification_async(action, users):
    if action == PRODUCT_REQUEST:
        from firebase_admin.messaging import Message, Notification
        devices = FCMDevice.objects.filter(user__id__in=users)
        message = Message(notification=Notification(
            title='Solicitud de Producto',
            body='Notificacion Enviada'
        ))
        devices.send_message(message)
