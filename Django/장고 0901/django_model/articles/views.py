from django.shortcuts import render, redirect
import random
from .models import Post 

def lotto(request):
    lotto_numbers = random.sample(range(1,46),6)
    context = {
        'lotto_numbers' : lotto_numbers,
    }
    return render(request, 'articles/lotto.html', context)

#모든 게시글의 목록을 보여주는 부분
def index(request):
    # 모든 게시글의 데이터가 필요
    # 1. 모든 데이터를 확보
    posts = Post.objects.all()
    # 2. 확보한 데이터를 template에 보여줘야 한다.
    # 확보한 데이터를 템플릿으로 전달할 필요가 있다.
    context = {
        'posts' : posts
    }
    return render(request, 'articles/index.html', context)

def hello(request,name,age):
    print(name)
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'articles/hello.html', context)

#new = 글쓰기 버튼을 눌렀을 때 사용자 입력 페이지(글쓰기 페이지) 응답으로 전달
def new(request):
    return render(request, 'articles/new.html')

# 사용자가 작성한 데이터를 받아서 DB에 저장하는 역할
def create(request):
    #데이터를 저장하기 위해서는 사용자의 데이터를 확보
    #print(request.GET)
    
    #GET 요청일 때 데이터를 받는 방법
    #title = request.GET.get('title')
    #content = request.GET.get('content')

    #POST 요청으로 바꿨을 때 수정되는 부분
    #POST요청일 때 데이터를 받는 방법
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title, content, '<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    #확보한 데이터를 DB에 저장

    #데이터를 DB에 저장하는 방법은 3가지
    # 1. POST 클래스의 빈 인스턴스를 생ㅇ성
    
    post = Post()
    post.title = title
    post.content = content
    post.save()  # DB저장

    # 2. POST클래스의 인스턴스를 생성 
    
    #post = Post(title=title, content=content)
    #post.save()

    # 3번 방법 (Queryset API create 메서드를 이용한다.)
    # post = Post.objects.create(title=title, content=content)

    # 글 작성을 완료하고 나면 다음 뜨는 페이지
    # 방법 1번 index 페이지로 이동해서 전체 데이터 목록을 보자!
    return redirect('articles:detail', post.pk)

def detail(request, post_id):
    #Post.objects.get(컬럼명=찾는 값)
    #사용자가 무슨 글을 클릭했는지?
    # => 사용자가 클릭한 글 정보를 전달받아야 함. 
    # ==> 주소로 글의 정보를 전달 받아야 함 (Variable routing 이용)
    # 글을 클릭할 떄 전달 => query api에서 get 메소드는 유일한 값을 이용해서 데이터를 찾음
    # 글을 클릭하는 index.html 에서 id를 주소에 넘겨준다.
    # 넘겨준 주소를 변수로 사용해야 하기 때문에 urls.py에서 변수 설정을 해준다
    # urls.py로 부터 넘어오는 변수를 첫 번째 인자로 받아준다. (이름은 반드시 동일) 
    # 그 값이 post_id <- 사용자가 클릭한 글의 아이디
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'articles/detail.html',context)

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'articles/edit.html', context)

def update(request, post_id):
    #1. 수정할 글 데이터를 찾아온다.
    post = Post.objects.get(pk=post_id)
    #2. 수정한다.
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    #3. 저장한다.
    post.save()
    #4. 글 수정을 완료 후 글 디테일 페이지로 이동한다.
    return redirect('articles:detail', post.pk )

def delete(request, post_id):
    #POST 요청일때만 삭제하게 만들기 
    if request.method == 'POST':
    # 삭제할 글 데이터를 찾아온다
        post = Post.objects.get(pk = post_id)
    # 삭제한다.
        post.delete()
    return redirect('articles:index')

# Create your views here.
