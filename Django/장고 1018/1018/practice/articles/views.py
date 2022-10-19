from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Article,Comment
from .serializers import ArticleListSerializer, ArticleSerializer,CommentSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def article_cr(request):
    if request.method == 'GET' :
        articles = get_list_or_404(Article)
        serialier = ArticleListSerializer(articles, many =True)
        return Response(serialier.data)
    
    elif request.method == 'POST':
        serialier = ArticleListSerializer(data=request.data)
        if serialier.is_valid(raise_exception= True):
            serialier.save()
            return Response(serialier.data, status.HTTP_201_CREATED )


@api_view(['GET', 'PUT', 'DELETE'])
def article_rud(request, article_pk):
    articles = get_object_or_404(Article, pk = article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(articles, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        articles.delete()
        return Response({'id':article_pk}, status= status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def comment_rc(request,comments_pk):
    comments = get_object_or_404(Comment, pk = comments_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(comments)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comments.delete()
        return Response({'id' : comments_pk}, status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def comment_c(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)