from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """
    A preset tag used to label and filter posts.
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """
    A blog post about a video game, board game, or tabletop game.
    """

    GAME_TYPES = [
        ('video', 'Video Game'),
        ('board', 'Board Game'),
        ('tabletop', 'Tabletop Game'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    game_type = models.CharField(
        max_length=20, choices=GAME_TYPES, default='video'
    )
    excerpt = models.CharField(max_length=240, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name='posts', blank=True
    )
    image = models.ImageField(
        upload_to='posts/', blank=True, null=True
    )
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Automatically create a unique slug from the title.
        If one doesn't exist, generates it and ensures uniqueness.
        """
        if not self.slug:
            base_slug = slugify(self.title) or 'post'
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(
                pk=self.pk
            ).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return the absolute URL for this post detail page."""
        from django.urls import reverse
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    """A user comment on a blog post."""

    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    body = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.body[:20]}... by {self.author}"


class Like(models.Model):
    """A like on a blog post. Each user can only like a post once."""

    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user} likes {self.post}"
