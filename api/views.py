from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, PostDetailSerializer, ReviewCreateSerializer
from rest_framework import generics
from articles.models import Post


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        articles = Post.objects.all()
        return articles


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        articles = Post.objects.all()
        return articles


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к посту"""
    serializer_class = ReviewCreateSerializer
    # permission_classes = [IsAuthenticated]
