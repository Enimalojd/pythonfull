from rest_framework import serializers

from core.user.serializers import UserSerializer
from core.user.models import User


class RegisterSerializer(UserSerializer):
    '''Сериализатор регистрации новых пользователей'''
    # пароль должен быть минимум 8 символов, но не больше 128 символов
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email',
                  'username', 'first_name', 'last_name',
                  'password']

        def create(self, validated_data):
            # Используем тот же метод для создания пользователя, который использовали в UserManager

            return User.objects.create_user(**validated_data)
