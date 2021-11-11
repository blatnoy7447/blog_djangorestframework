from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)


class Post(models.Model):
    """Посты"""
    title = models.CharField(max_length=155)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Отзывы"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField("Сообщение", max_length=5000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    created_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    update_date = models.DateTimeField("Изменен", auto_now=True)
    parent = models.ForeignKey('self',
                               verbose_name="Родитель",
                               on_delete=models.CASCADE,
                               related_name='children',
                               null=True,
                               blank=True
                               )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
