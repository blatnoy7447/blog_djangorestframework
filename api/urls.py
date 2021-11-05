from django.urls import path
from .views import PostListView, PostDetailView, ReviewCreateView


urlpatterns = [
    path('post/', PostListView.as_view()),
    path('post-detail/<int:pk>/', PostDetailView.as_view()),
    path('reviews/<int:pk>/', ReviewCreateView.as_view())
]
