from django.shortcuts import render, redirect
from .forms import ArticleForm, Article
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.
#def new(request):
#    form = ArticleForm()
#    context = {
#        'form' : form,
#    }
#    return render(request, 'articles/new.html', context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        #new
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html' , context)

@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance = article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

@require_safe 
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@require_safe 
def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html',context)

@require_POST
def delete(request, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id = article_id)
        article.delete()
    return redirect('articles:index')