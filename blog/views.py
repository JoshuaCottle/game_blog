from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CommentForm, PostForm, SignUpForm
from .models import Like, Post


class PostListView(ListView):
    """Display a list of all published blog posts."""

    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """Display a single blog post with its comments and like status."""

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = post.comments.filter(active=True)
        context['comment_form'] = CommentForm()
        if self.request.user.is_authenticated:
            context['liked'] = Like.objects.filter(
                post=post, user=self.request.user
            ).exists()
        else:
            context['liked'] = False
        return context

    def post(self, request, *args, **kwargs):
        """Handle comment form submission when a user adds a comment."""
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            messages.success(
                request, 'Your comment has been posted successfully!'
            )
        return redirect('blog:post_detail', slug=self.object.slug)


class PostCreateView(LoginRequiredMixin, CreateView):
    """Allow logged-in users to create a new blog post."""

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request, 'Your post has been created successfully!'
        )
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allow post authors to edit their own posts."""

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        messages.success(
            self.request, 'Your post has been updated successfully!'
        )
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allow post authors to delete their own posts."""

    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 'Your post has been deleted successfully!'
        )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().author == self.request.user


class SignUpView(CreateView):
    """Handle new user registration."""

    form_class = SignUpForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your account has been created! You can now log in.',
        )
        return super().form_valid(form)


@login_required
def toggle_like(request, slug):
    """
    Toggle like/unlike for a post.
    Creates a like if it doesn't exist, removes it if it does.
    """
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        messages.info(request, 'You unliked this post.')
    else:
        messages.success(request, 'You liked this post!')
    return redirect('blog:post_detail', slug=slug)
