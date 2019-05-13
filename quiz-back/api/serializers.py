from rest_framework import serializers
from api.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(read_only=True, required=False)
    # created_by = UserSerializer(read_only=True, required=False)
    # title = serializers.CharField(required=False)
    # body = serializers.CharField(required=False)
    # like_count = serializers.IntegerField(required=True)
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('created_at', 'body', 'like_count', 'id', 'title', 'created_by')
        read_only_fields = ('created_at', 'created_by', 'id')
        required_field_names = ('body', 'title')
