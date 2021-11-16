from rest_framework import serializers
from articles.models import *


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)
    author = serializers.StringRelatedField(many=False)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('text', 'children', 'author')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "summary", "img")


class PostDetailSerializer(serializers.ModelSerializer):
    """Полный пост"""
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
