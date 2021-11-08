from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PostSerializer, PostDetailSerializer, ReviewCreateSerializer
from rest_framework import generics, viewsets
from articles.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class PostViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Post.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = PostDetailSerializer(post)
#         return Response(serializer.data)


# class PostListView(generics.ListAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         posts = Post.objects.all()
#         return posts
#
#
# class PostCreateView(generics.CreateAPIView):
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         posts = Post.objects.all()
#         return posts
#
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         posts = Post.objects.all()
#         return posts


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к посту"""
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]
