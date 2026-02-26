from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts.
    """

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
            'tags': forms.SelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    """
    Form for users to add comments to posts.
    """

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }


class SignUpForm(UserCreationForm):
    """User registration form with email field added."""

    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        # Add more email validation if needed
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required.')
        # Prevent XSS by escaping username
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
