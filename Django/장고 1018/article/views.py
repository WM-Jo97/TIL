from os import stat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article

# Create your views here.

@api_view(['GET','POST'])
def article_cr(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def article_ru(request, article_pk):
    articles = Article.objects.get(pk = article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(articles, data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        articles.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)