from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from core.user.serializers import UserSerializer
from core.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = get_object_or_404(User, public_id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
