from rest_framework import serializers
from .models import Article

# 여러 데이터의 정보를 보여줄 때 사용하는 serializer 
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)


# detail 한 내용을 보여주는 serializer 사용
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'