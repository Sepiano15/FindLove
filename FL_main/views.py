from django.shortcuts import render, redirect, get_object_or_404 #render : 데이터를 받아온 뒤 html로 데이터를 보내기 위한 함수
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages #에러메시지
from blogapp.forms import CreateBlog, BlogCommentForm, UserForm, LoginForm
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

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if 'id_configure' in request.POST:
            if len(form.errors)>=1: #id오류가 나면
                messages.error(request,'중복된 아이디입니다. 아이디를 새로 입력해주세요.')
                return redirect('signup')
            else:
                messages.error(request,'사용할 수 있는 아이디입니다.')
                return redirect('signup')

        elif 'Signup' in request.POST:
            if form.is_valid():
                #if request.POST["password"] == request.POST["verify_password"]: #비밀번호 재확인
                new_user = User.objects.create_user(**form.cleaned_data)
                auth.login(request, new_user)
                return redirect('index')
            else: #form.is_valid가 안된다는건 아이디에 오류가 있다는 뜻이다.
                messages.error(request,'아이디 중복확인을 해주세요.')
                return redirect('signup')

        return redirect('signup')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})

def about(request):
    return render(request, 'about.html')