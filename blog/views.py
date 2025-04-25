# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Category, UserProfile
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserUpdateForm, PostForm
from .models import Comment
from .forms import CommentForm


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
    Displays a single blog post and handles comment submission.
    """
    post = get_object_or_404(Post, pk=post_id)

    # Only get approved comments
    comments = post.comments.filter(parent=None, is_approved=True)
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

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
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
    Display and update user profile.
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

    # Get user's posts
    user_posts = Post.objects.filter(author=request.user)

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


def author_profile(request, username):
    """
    View another user's profile and posts.
    """
    author = get_object_or_404(User, username=username)
    author_posts = Post.objects.filter(author=author)

    context = {
        'author': author,
        'author_posts': author_posts
    }

    return render(request, 'blog/author_profile.html', context)
