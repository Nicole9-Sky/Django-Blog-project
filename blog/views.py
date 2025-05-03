# blog/views.py

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .forms import SearchForm
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserUpdateForm, PostForm
from .models import Comment
from .models import Like
from .models import Post, Tag



def tag_posts(request, tag_slug):
    """
    Display posts filtered by tag
    """
    from django.db.models import Count

    tag = get_object_or_404(Tag, slug=tag_slug)
    # Annotate with like counts
    posts_list = Post.objects.filter(tags=tag).annotate(likes_count=Count('likes')).order_by('-pub_date')

    # Set up pagination
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'tag': tag
    }

    return render(request, 'blog/tag_posts.html', context)


def post_list(request):
    """
    Displays a paginated list of blog posts with featured posts carousel.
    """
    from django.db.models import Count

    # Get featured posts with like counts
    featured_posts = Post.objects.filter(is_featured=True).annotate(
        likes_count=Count('likes')
    ).order_by('-pub_date')

    # Get regular posts with like counts (excluding featured ones)
    regular_posts_list = Post.objects.filter(is_featured=False).annotate(
        likes_count=Count('likes')
    ).order_by('-pub_date')

    # Get the most used tags (limited to 20)
    tags = Tag.objects.annotate(
        num_posts=Count('posts')
    ).order_by('-num_posts')[:20]

    # Set up pagination for regular posts only
    paginator = Paginator(regular_posts_list, 6)
    page = request.GET.get('page')

    try:
        regular_posts = paginator.page(page)
    except PageNotAnInteger:
        regular_posts = paginator.page(1)
    except EmptyPage:
        regular_posts = paginator.page(paginator.num_pages)

    context = {
        'featured_posts': featured_posts,
        'posts': regular_posts,
        'tags': tags
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):
    """
    Displays a single blog post and handles comment submission.
    """
    post = get_object_or_404(Post, pk=post_id)

    # Increment the view count - only once per session
    session_key = f'viewed_post_{post.id}'
    if not request.session.get(session_key, False):
        post.increment_view_count()
        request.session[session_key] = True

    # Add a liked_by_user property to the post
    if request.user.is_authenticated:
        post.liked_by_user = post.likes.filter(user=request.user).exists()
    else:
        post.liked_by_user = False

    # Only get approved comments
    comments = post.comments.filter(parent=None, is_approved=True)

    # Add a liked_by_user property to each comment and reply
    if request.user.is_authenticated:
        for comment in comments:
            comment.liked_by_user = comment.likes.filter(user=request.user).exists()
            for reply in comment.replies.all():
                reply.liked_by_user = reply.likes.filter(user=request.user).exists()
    else:
        for comment in comments:
            comment.liked_by_user = False
            for reply in comment.replies.all():
                reply.liked_by_user = False

    new_comment = None
    comment_form = None

    if request.user.is_authenticated:
        # Comment form processing
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user

                # Handle reply to comment
                parent_id = request.POST.get('parent_id')
                if parent_id:
                    new_comment.parent = Comment.objects.get(id=parent_id)

                # Save the comment (is_approved defaults to False in the model)
                new_comment.save()

                # Notify user that comment is pending approval
                messages.success(request, 'Your comment has been submitted and is awaiting approval.')
                return redirect('post_detail', post_id=post.id)
        else:
            comment_form = CommentForm()

    # Get related posts by tags (up to 3)
    related_posts = []
    if post.tags.exists():
        tag_ids = post.tags.values_list('id', flat=True)
        related_posts = Post.objects.filter(tags__in=tag_ids).exclude(id=post.id).distinct()[:3]

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'related_posts': related_posts,  # Add related posts based on tags
    }
    return render(request, 'blog/post_detail.html', context)



@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    # Stricter permission check
    if not (comment.author == request.user or request.user.is_staff):
        messages.error(request, "You cannot delete someone else's comment!")
        return redirect('post_detail', post_id=comment.post.id)

    post_id = comment.post.id

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'The comment has been deleted!')
        return redirect('post_detail', post_id=post_id)

    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})



def register(request):
    """
    Handle user registration.
    """
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, f'Account created for {user.username}! You are now logged in.')
            return redirect('post_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    """
    Handle user login.
    """
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                # Get the next parameter or default to post_list
                next_page = request.GET.get('next', 'post_list')
                return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('post_list')



@login_required
def profile(request):
    """
    Display and update user profile with paginated posts.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    # Get user's posts with pagination
    user_posts_list = Post.objects.filter(author=request.user)

    # Debug: Print the count of posts found (you can remove this after fixing)
    print(f"Found {user_posts_list.count()} posts for user {request.user.username}")

    # Set up pagination
    paginator = Paginator(user_posts_list, 6)  # Show 6 posts per page
    page = request.GET.get('page')

    try:
        user_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        user_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        user_posts = paginator.page(paginator.num_pages)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_posts': user_posts
    }

    return render(request, 'blog/profile.html', context)

@login_required
def create_post(request):
    """
    Create a new blog post.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Post'})


@login_required
def update_post(request, post_id):
    """
    Update an existing blog post.
    """
    post = get_object_or_404(Post, pk=post_id)

    # Check if the user is the author
    if post.author != request.user:
        messages.error(request, "You cannot edit someone else's post!")
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Update Post'})


@login_required
def delete_post(request, post_id):
    """
    Delete a blog post.
    """
    post = get_object_or_404(Post, pk=post_id)

    # Check if the user is the author
    if post.author != request.user:
        messages.error(request, "You cannot delete someone else's post!")
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def like_post(request, post_id):
    """
    Toggle like status for a post
    """
    post = get_object_or_404(Post, pk=post_id)
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post,
        defaults={'comment': None}
    )

    # If not created, it means the like already existed, so we remove it
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    # Get updated count
    like_count = post.likes.count()

    # Return JSON response
    return JsonResponse({
        'liked': liked,
        'like_count': like_count
    })


@login_required
def like_comment(request, comment_id):
    """
    Toggle like status for a comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    like, created = Like.objects.get_or_create(
        user=request.user,
        comment=comment,
        defaults={'post': None}
    )

    # If not created, it means the like already existed, so we remove it
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    # Get updated count
    like_count = comment.likes.count()

    # Return JSON response
    return JsonResponse({
        'liked': liked,
        'like_count': like_count
    })




def search_posts(request):
    """
    Search for posts by title, content, author username, or tags with pagination.
    """
    from django.db.models import Count

    search_form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    results_list = []

    if query:
        # Search in title, content, author's username, and tags
        # And annotate with like counts
        results_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().annotate(likes_count=Count('likes')).order_by('-pub_date')

    # Set up pagination
    paginator = Paginator(results_list, 6)  # Show 6 results per page
    page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        'search_form': search_form,
        'query': query,
        'results': results
    }

    return render(request, 'blog/search_results.html', context)



def author_profile(request, username):
    """
    View another user's profile and posts with pagination.
    """
    from django.db.models import Count

    author = get_object_or_404(User, username=username)

    # Make sure we're filtering correctly by author and annotating with like counts
    author_posts_list = Post.objects.filter(author=author).annotate(likes_count=Count('likes')).order_by('-pub_date')

    # Set up pagination
    paginator = Paginator(author_posts_list, 6)  # Show 6 posts per page
    page = request.GET.get('page')

    try:
        author_posts = paginator.page(page)
    except PageNotAnInteger:
        author_posts = paginator.page(1)
    except EmptyPage:
        author_posts = paginator.page(paginator.num_pages)

    context = {
        'author': author,
        'author_posts': author_posts
    }

    return render(request, 'blog/author_profile.html', context)