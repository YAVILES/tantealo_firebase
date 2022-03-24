from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import routers

from apps.system.views import UserView

router = routers.SimpleRouter()
router.register(r'devices', FCMDeviceAuthorizedViewSet)
router.register(r'users', UserView)

urlpatterns = [
]

urlpatterns += router.urls
