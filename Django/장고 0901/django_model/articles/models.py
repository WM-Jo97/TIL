from turtle import title
from django.db import models

class Post(models.Model):
    # CharField / TextField 문자를 저장하기 위한 필드
    # CharField : 글자제한 / TextField : 글자 제한이 없을 때 사용
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
