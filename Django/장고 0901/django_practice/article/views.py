from ssl import HAS_TLSv1_1
from django.shortcuts import render

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'articles/index.html', context)

def create(request):
    return render(request, 'article/index.html')