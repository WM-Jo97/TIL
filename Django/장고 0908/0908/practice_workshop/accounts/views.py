from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
        'title' : '회원가입 페이지',
        'btn_title' : '회원가입'
    }

    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:login_index')
    else: form = AuthenticationForm()

    context = {
        'form' : form,
        'title' : '로그인 페이지',
        'btn_title' : '로그인'
    }
    return render(request,'accounts/form.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('accounts:index')

def index(request):
    return render(request, 'accounts/index.html')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
        'title' : '회원정보 수정',
        'btn_title' : '수정'
    }
    return render(request, 'accounts/form.html' , context)

def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('accounts:index')

def login_index(request):
    return render(request, 'accounts/login_index.html')


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
        'title' : '비밀번호 수정',
        'btn_title' : '수정'
    }

    return render(request, 'accounts/form.html', context)