from rest_framework import serializers
from .models import Article


class ArticleSerializer(__(b)__):

    class Meta:
        model = Article
        fields = '__all__'