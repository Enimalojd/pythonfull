from rest_framework import routers

from .auth.viewsets.register import RegisterViewSet
from .user.viewsets import UserViewSet

router = routers.SimpleRouter()

# User router
router.register(r'user', UserViewSet, basename='user')

# Auth router
router.register(r'auth/register', RegisterViewSet,
                basename='auth-register')

api_router = router
