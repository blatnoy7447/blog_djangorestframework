from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .serializers import PostSerializer, PostDetailSerializer, ReviewCreateSerializer
from rest_framework import generics, viewsets, status
from articles.models import Post, Review


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {'destroy': [IsAdminUser],
                                    'list': [AllowAny]}

    def list(self, request, *args, **kwargs):
        return super(PostViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class PostDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {'destroy': [IsAdminUser],
                                    'create': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    "partial_update": [IsAdminUser],
                                    'list': [AllowAny]}

    def create(self, request, *args, **kwargs):
        return super(PostDetailViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PostDetailViewSet, self).retrieve(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к посту"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        user = request.user.id
        request.data['author'] = user
        return super(ReviewCreateViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(ReviewCreateViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
