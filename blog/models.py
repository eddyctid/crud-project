from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    ) # new
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse("blog_detail_view", kwargs={"pk": self.pk})

