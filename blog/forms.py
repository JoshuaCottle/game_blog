from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""

    class Meta:
        model = Post
        fields = [
            'title',
            'game_type',
            'excerpt',
            'tags',
            'image',
            'content',
            'published',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    """Form for users to add comments to posts."""

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }


class SignUpForm(UserCreationForm):
    """User registration form with email field added."""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
