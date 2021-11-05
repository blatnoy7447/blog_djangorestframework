from rest_framework import serializers
from articles.models import Post, Review


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'summary')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    class Meta:
        model = Review
        fields = ('text', 'parent')


class PostDetailSerializer(serializers.ModelSerializer):
    """Полный пост"""
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"



