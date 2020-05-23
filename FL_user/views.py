from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404 #render : 데이터를 받아온 뒤 html로 데이터를 보내기 위한 함수
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib import auth
from django.contrib import messages #에러메시지
from .forms import UserForm, LoginForm, UserCreationForm, UserChangeForm
from .models import UserInfo
from django.contrib.auth import login, authenticate

user='0'
password='0'
# Create your views here.
def signup(request):
	if request.method == "POST":
		request.POST = request.POST.copy()
		request.POST['username']=user
		request.POST['password']=password
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			#new_user = UserInfo.objects.create_user(**form.cleaned_data)
			return redirect('index')
		else: #form.is_valid가 안된다는건 아이디에 오류가 있다는 뜻이다.
		    messages.error(request,'정보를 빠짐없이 입력해주세요.')
		    return render(request, 'signup_cert.html',{'form': form})

		messages.error(request,'알 수 없는 오류 입니다.')
		return redirect('signup')
	else:
		form = UserForm()
		return render(request, 'signup.html', {'form': form})

def login_cert(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        global user, password
        search = UserInfo.objects.filter(username=request.POST['username'])
        if(len(search)==0):
            messages.error(request,'사용할 수 있는 아이디입니다.')
            user = request.POST['username']
            password = request.POST['password']
            return render(request, 'signup_cert.html',{'form': form})
        else:
            messages.error(request,'중복된 아이디입니다. 아이디를 새로 입력해주세요.')
            return redirect('signup')	