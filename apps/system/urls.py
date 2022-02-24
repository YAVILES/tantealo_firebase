from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
]

urlpatterns += router.urls
