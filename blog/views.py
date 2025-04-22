# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    """
    Displays a list of all blog posts.
    """
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    """
    Displays a single blog post.
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

# You could add a view for categories later, e.g.:
# def category_posts(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     posts = Post.objects.filter(category=category)
#     context = {
#         'category': category,
#         'posts': posts
#     }
#     return render(request, 'blog/category_posts.html', context)