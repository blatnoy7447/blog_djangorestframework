from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=155)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',
                               default=None,
                               on_delete=models.CASCADE,
                               related_name='children',
                               null=True,
                               blank=True
                               )

    def __str__(self):
        return self.comment
