from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            # 작성자를 저장하기 위해 commit = False
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    # print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 댓글 작성을 위한 입력 폼
    comment_form = CommentForm()

    # 댓글을 보여주기 위해 DB에서 댓글 정보를 가져온다.
    # Comment.objects.all()  # 1번글에서 2번글의 댓글까지 보여짐. 이렇게 하면 안됨
    # Comment.objects.get()   # 댓글은 하나만 작성되지 않음 (N개가 작성됨) get으로 찾으면 안됨
    comments = Comment.objects.filter(article=article)
    context = {
        'article': article,
        # 반드시 html에서 사용할 수 있도록 comment_form을 전달해야 함
        'comment_form': comment_form,  
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 글쓴이가 아닌 사람이 삭제하려고 하는 것을 방지
    if request.user != article.author:
        return redirect('articles:detail', article.pk)

    if request.user.is_authenticated:
        article.delete()

    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # 글쓴이가 아닌 사람이 수정하려고 하는 것을 방지
    if request.user != article.author:
        return redirect('articles:detail', article.pk)

    if request.method == 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comment_create(request, article_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=article_pk)  # 댓글의 글 데이터를 넣기 위해 글 정보를 불러와야 함
    
    if comment_form.is_valid():
        # 그냥 save를 하면 not null constraint failed 
        comment = comment_form.save(commit=False)  # comment : DB에 저장되기 전 사용자가 입력한 comment 데이터의 인스턴스
        comment.article = article                  # 글 정보를 직접 입력
        comment.save()                             # 최종 저장
        return redirect('articles:detail', article_pk)

    # 유효성 검사를 통과하지 못하는 경우
    # 리다이렉트를 하게 되면 에러정보가 전달되지 못함
    # 그래서 직접 렌더를 해야한다.
    comments = Comment.objects.filter(article=article)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def comment_delete(request, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    # 어떤 댓글을 지우죠????
    comment = Comment.objects.get(pk=comment_pk)
    article = comment.article  # 삭제하기 전에 게시글 정보를 저장한다. (redirect 할 때 필요해서)
    comment.delete()

    return redirect('articles:detail', article.pk)