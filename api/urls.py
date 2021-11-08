from django.urls import path
from .views import ReviewCreateView, PostViewSet


post_list = PostViewSet.as_view({
    'get': 'list',
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('post-set/', post_list, name='post-list'),
    path('post-set/<int:pk>/', post_detail, name='post-detail'),
    path('reviews/', ReviewCreateView.as_view())
]
