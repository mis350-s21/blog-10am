from django.db import models

# Create your models here.
class Post(models.Model):

    STATUS = (
        (0, "Unpublished"),
        (1, "Published"),
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title}: created at {self.created_at}"