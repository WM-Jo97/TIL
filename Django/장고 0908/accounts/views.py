
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next = request.GET.get('next')
            return redirect(next or 'articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
        'title' : '로그인 페이지',
        'btn_title' : '로그인',
    }

    return render(request, 'accounts/form.html',context)

@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
        'title' : '회원가입 페이지',
        'btn_title' : '회원가입'
    }
    return render(request, 'accounts/form.html' , context)

@login_required
@require_POST
def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
        'title' : '회원정보 수정',
        'btn_title' : '수정'
    }
    return render(request,'accounts/form.html', context)

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
        'title' : '비밀번호 수정',
        'btn_title' : '수정'
    }

    return render(request, 'accounts/form.html', context)