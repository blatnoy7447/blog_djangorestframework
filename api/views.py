from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import generics
from articles.models import Article, Comment


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = Article.objects.all()
        return articles


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        articles = Article.objects.all()
        return articles


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        comments = Comment.objects.all()
        return comments
