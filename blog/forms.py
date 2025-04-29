# blog/forms.py (updated)

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment, Tag  # Import Tag here
from django.utils.text import slugify


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'website')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False,
                           help_text="Enter tags separated by commas",
                           widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'}))

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image', 'tags')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8}),
        }

    def clean_tags(self):
        if self.cleaned_data['tags']:
            return [tag.strip() for tag in self.cleaned_data['tags'].split(',')]
        return []

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

            # Clear existing tags and add new ones
            post.tags.clear()
            tag_list = self.cleaned_data['tags']

            if tag_list:
                for tag_name in tag_list:
                    if tag_name:
                        # Create or get tag
                        slug = slugify(tag_name)
                        tag, created = Tag.objects.get_or_create(
                            slug=slug,
                            defaults={'name': tag_name}
                        )
                        post.tags.add(tag)

        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a comment...'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search posts...',
            'class': 'search-input'
        })
    )