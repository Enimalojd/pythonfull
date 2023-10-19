from rest_framework_nested import routers
from .auth.viewsets import LoginViewSet, RefreshViewSet
from .auth.viewsets.register import RegisterViewSet
from .comment.viewsets import CommentViewSet
from .post.viewsets import PostViewSet
from .user.viewsets import UserViewSet

router = routers.SimpleRouter()

# User router
router.register(r'user', UserViewSet, basename='user')

# Auth router
router.register(r'auth/register', RegisterViewSet,
                basename='auth-register')
router.register(r'auth/login', LoginViewSet,
                basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet,
                basename='auth-refresh')
# Post router
router.register(r'post', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')

posts_router.register(r'comment', CommentViewSet, basename='post-comment')

api_router = router
