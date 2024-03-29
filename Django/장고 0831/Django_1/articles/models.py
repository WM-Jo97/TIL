from turtle import update
from venv import create
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    #필드 이름      # 타입
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
