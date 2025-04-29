# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing paths
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Authentication paths
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Profile paths
    path('profile/', views.profile, name='profile'),
    path('author/<str:username>/', views.author_profile, name='author_profile'),

    # Post management paths
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/update/', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', views.search_posts, name='search_posts'),
    path('tag/<slug:tag_slug>/', views.tag_posts, name='tag_posts'),
]
