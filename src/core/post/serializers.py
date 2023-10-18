from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='public_id')
    liked = serializers.SerializerMethodField()
    liked_count = serializers.SerializerMethodField()

    def get_liked(self, instance):
        request = self.context.get('request', None)

        if request is None or request.user.is_anonymous:
            return False

        return request.user.has_liked(instance)

    def get_likes_count(self, instance):
        return instance.liked_by.count()

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("Вы не можете создать пост для другого пользователя")

        return value

    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'liked',
                  'likes_count', 'created', 'updated']
        read_only_fields = ["edited"]
