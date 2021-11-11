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

    def create(self, request, *args, **kwargs):
        return super(PostViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PostViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

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


class ReviewCreateView(viewsets.ModelViewSet):
    """Добавление отзыва к посту"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        user = request.user.id
        request.data['author'] = user
        return super(ReviewCreateView, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(ReviewCreateView, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
