from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from drf_api.users.api.views import UserViewSet, UserViewSetTwo

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("users-two", UserViewSetTwo, basename="users")

app_name = "api"
urlpatterns = router.urls
