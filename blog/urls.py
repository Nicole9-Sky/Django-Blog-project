# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Path for the list of posts (homepage)
    path('', views.post_list, name='post_list'),
    # Path for a single post, expects an integer post_id
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # You could add a category path later, e.g.:
    # path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]