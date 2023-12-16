from rest_framework import serializers
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    author = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    author = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Ad
        fields = ["pk", "title", "price", 'created_at', 'author']


class AdDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    author = serializers.SlugRelatedField(slug_field="email", read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Ad
        fields = "__all__"
