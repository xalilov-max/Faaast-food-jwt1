from django.urls import path
from .views import (
    TopicListCreateView,
    CommentListCreateView,
    ReplyListCreateView,
    RegisterView
)

urlpatterns = [
    path('topics/', TopicListCreateView.as_view(), name='topics'),
    path('comments/', CommentListCreateView.as_view(), name='comments'),
    path('replies/', ReplyListCreateView.as_view(), name='replies'),
    path('register/', RegisterView.as_view(), name='register'),
]
