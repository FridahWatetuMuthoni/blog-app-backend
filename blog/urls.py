from django.urls import path
from .views import PostDetail, PostList

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('<str:pk>/', PostDetail.as_view(), name='post_detail'),
]