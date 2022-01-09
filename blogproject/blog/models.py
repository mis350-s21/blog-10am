from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.
class Post(models.Model):

    STATUS = (
        (0, "Unpublished"),
        (1, "Published"),
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100) #, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}: created at {self.created_at}"

class Comment(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
