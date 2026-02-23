from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Tag, Comment


class PostModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='pass'
        )
        self.tag = Tag.objects.create(name='RPG')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            published=True
        )
        self.post.tags.add(self.tag)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_slug_auto(self):
        self.assertTrue(self.post.slug.startswith('test-post'))

    def test_post_tag_relationship(self):
        self.assertIn(self.tag, self.post.tags.all())


class PostListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='pass'
        )
        Post.objects.create(
            title='Visible', content='...', author=self.user, published=True
        )
        Post.objects.create(
            title='Hidden', content='...', author=self.user, published=False
        )

    def test_post_list_view_status(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_shows_only_published(self):
        response = self.client.get(reverse('blog:post_list'))
        posts = response.context['posts']
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts[0].title, 'Visible')


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='pass'
        )
        self.post = Post.objects.create(
            title='Test', content='...', author=self.user, published=True
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user, body='Nice!', active=True
        )

    def test_comment_str(self):
        self.assertIn('Nice!', str(self.comment))

    def test_comment_active(self):
        self.assertTrue(self.comment.active)
