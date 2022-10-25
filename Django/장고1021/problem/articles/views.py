from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

# Q 1.
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # Q 2.
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            Response(serializer.data)

@api_view(['GET','POST','DELETE']) 
def article_detail(request,article_pk):
    if request.method == 'GET':
        article = Article.objects.all(pk = article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)