# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse # new

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
        title="A good title",
        body="Nice body content",
        author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/blogpost/1/")

    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self): # new
        response = self.client.get("/blogpost/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self): # new
        response = self.client.get(reverse("blog_list_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "homepage.html")

    def test_post_detailview(self): # new
        response = self.client.get(reverse("blog_detail_view",
        kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/blogpost/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "blogdetail.html")

    def test_post_createview(self): # new
        response = self.client.post(
        reverse("blog_create_view"),
        {
        "title": "New title",
        "body": "New text",
        "author": self.user.id,
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self): # new
        response = self.client.post(
        reverse("blog_update_view", args="1"),
        {
        "title": "Updated title",
        "body": "Updated text",
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")
        
    def test_post_deleteview(self): # new
        response = self.client.post(reverse("blog_delete_view", args="1"))
        self.assertEqual(response.status_code, 302)