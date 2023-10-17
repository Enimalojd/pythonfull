from rest_framework import routers
from user.viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]