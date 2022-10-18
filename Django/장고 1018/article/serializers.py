from dataclasses import field
from rest_framework import serializers
from .models import Article

#여러 데이터의 정보를 보여줄 때
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title')

#디테일한 내용을 보여줄 떄
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

