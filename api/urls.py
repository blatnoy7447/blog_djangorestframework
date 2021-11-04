from django.urls import path
from .views import ArticleListView, CommentView, ArticleDetailView


urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('article-detail/<int:pk>/', ArticleDetailView.as_view()),
    path('comments/<int:pk>/', CommentView.as_view())
]
