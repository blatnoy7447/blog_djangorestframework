from django.urls import path
from .views import ReviewCreateViewSet, PostViewSet, PostDetailViewSet


post_list = PostViewSet.as_view({
    'get': 'list',
})
post_detail = PostDetailViewSet.as_view({
    'get': 'retrieve',
    # 'post': 'create',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
review_detail = ReviewCreateViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    # 'delete': 'destroy'
})
urlpatterns = [
    path('post/', post_list, name='post-list'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('reviews/<int:pk>/', review_detail, name='review-detail')
]
