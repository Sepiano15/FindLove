from django.shortcuts import render, redirect, get_object_or_404 #render : 데이터를 받아온 뒤 html로 데이터를 보내기 위한 함수
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages #에러메시지
from blogapp.forms import CreateBlog, BlogCommentForm
from FL_user.forms import LoginForm
from blogapp.models import Blog, Comment
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request,'사용자 이름과 비밀번호가 일치하지 않습니다.')
            return redirect('index')
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('index')

def about(request):
    return render(request, 'about.html')