from django.urls import path

from .views import (
    PostCreateView,  # Create new post
    PostDeleteView,  # Delete post
    PostDetailView,  # View post details
    PostListView,    # List all posts
    PostUpdateView,  # Edit post
    SignUpView,      # User registration
    toggle_like,     # Like/unlike post
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path(
        'post/<slug:slug>/',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'post/<slug:slug>/edit/',
        PostUpdateView.as_view(),
        name='post_update'
    ),
    path(
        'post/<slug:slug>/delete/',
        PostDeleteView.as_view(),
        name='post_delete'
    ),
    path('post/<slug:slug>/like/', toggle_like, name='post_like'),
    path('register/', SignUpView.as_view(), name='register'),
]
