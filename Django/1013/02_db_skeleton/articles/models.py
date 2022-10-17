from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    # 글 작성자를 저장하기 위해 FK 추가
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# 댓글 정보를 저장하기 위한 모델 클래스 작성
class Comment(models.Model):
    content = models.CharField(max_length=200)
    # 어떤 게시글에 댓글이 달렸는지 게시글 정보를 저장하기 위한 F.K.
    # FK는 1:N 관계에서 N에 위치하면 된다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content