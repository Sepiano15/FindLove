from django.shortcuts import render, redirect, get_object_or_404 #render : 데이터를 받아온 뒤 html로 데이터를 보내기 위한 함수
from .forms import CreateBlog, BlogCommentForm, UserForm, LoginForm #forms의 CreateBlog 클래스를 import하여 form을 불러온다.
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib import auth
from django.contrib import messages #에러메시지
import requests #json 파싱을 위해 import. pip로 따로 설치해주어야함.
import json #메시지를 보내기 위해 data리스트를 json의 형태로 변환.

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('blogMain')
        else:
            messages.error(request,'사용자 이름과 비밀번호가 일치하지 않습니다.')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('blogMain')

def show_profile(request):
    return render(request,'Show_Profile.html')

def modify_info(request):
    return render(request,'Modify_Info.html')


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
                return redirect('blogMain')
            else: #form.is_valid가 안된다는건 아이디에 오류가 있다는 뜻이다.
                messages.error(request,'아이디 중복확인을 해주세요.')
                return redirect('signup')

        return redirect('signup')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})

def write_profile(request):
    return render(request,'Write_profile.html')

def heartlist(request):
    return render(request,'Heartlist.html')

def success(request):
    return render(request,'Success.html')

def createBlog(request):
    if request.method == 'POST': #데이터가 POST방식으로 넘어오면
        #request.POST['author']=request.user.get_username()
        request.POST = request.POST.copy()
        #request.POST['author']=author_id
        form = CreateBlog(request.POST) #CreateBlog()폼에 값을 전달한 상태로 form 객체를 만든다.
        #print(form)
        #print(request.user.get_username())
        if form.is_valid(): #데이터들이 올바른 형식이라면
            form.save()#데이터베이스에 저장한다.
            #memo = form.save(commit = False)
            #memo.author=request.user.get_username()
            #memo.generate()
            return redirect('blogMain') #그 후 블로그 메인으로 간다.
        else:
            return redirect('index') #redirect는 단순히 특정 url이나 문서로 이동할 때 쓴다.
    else: #POST로 넘어오지 않았으면 [글쓰기]를 눌러서 들어온 것. 제출한 게 아님. 서버에 보내는 패킷이 없음.
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

    #form = CreateBlog() #form이라는 객체를 생성해서 폼을 불러들인다.
    #return render(request,'createBlog.html',{'form':form}) #render의 세 번째 인자는 불러들인 form을 넣는다. 이것은 딕셔너리 자료형이다. createBlog.html문서에서 장고 템플릿 변수를 이용하여 값을 출력할 수 있게된다.

def blogMain(request):
    blogs = Blog.objects.all() #DB에 이미 저장된 Blog객체 모두를 가리킨다. SQL에서 SELECT * 명령문과 같다.

    return render(request, 'blogMain.html', {'blogs': blogs}) #blogMain에 blogs객체를 넘겨준다.

def detail(request, document_id):
    document = get_object_or_404(Blog, pk=document_id) #pk는 DB의 주키이다.
    comments = Comment.objects.filter(document_id=document_id) #SQL의 SELECT WHERE조건문이다. 모델클래스.objects.filter와 같이 사용.

    if request.method == 'POST': #댓글을 작성하고 전송할경우
        comment_form = BlogCommentForm(request.POST) #작성한 댓글내용을 담을 객체
        comment_form.instance.author_id = request.user.id
        comment_form.instance.document_id = document_id

        if comment_form.is_valid():
            comment = comment_form.save()

            '''kakao
            content = comment_form.cleaned_data['comment_textfield'] #실제 댓글 폼에 입력된 데이터 comment_textfield에 해당하는 걸 받아온다.

            print(content)

            #login_request를 위해서 작성한다.
            login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

            client_id = '98d2a0df81acbf0575311dbc13e5544c'
            redirect_uri = 'http://127.0.0.1:8000/oauth'

            login_request_uri += 'client_id=' + client_id
            login_request_uri += '&redirect_uri=' + redirect_uri
            login_request_uri += '&response_type=code&scope=talk_message'

            #session에 REST key와 redirect uri를 등록한다.
            request.session['client_id'] = client_id
            request.session['redirect_uri'] = redirect_uri
            request.session['content'] = content

            return redirect(login_request_uri)
            '''
        else:
            return redirect('blogMain')

        comment_form = BlogCommentForm()
        comments = document_id.comments.all()
        context = {
            'blog_detail': document,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'detail.html', context)


    else: #댓글작성이 아니므로 블로그 상세내용만 보여줌
        comment_form = BlogCommentForm()

        context = {
            'blog_detail': document,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'detail.html', context)


def oauth(request):
    #code를 가져온다.
    code = request.GET['code']

    #세션에 등록된 REST key와 redirect uri를 가져다 쓴다.
    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')
    content = request.session.get('content')

    #access token uri을 작성한다. access_token을 받아오기 위한 uri이다.
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code

    #access_token을 가져온다.
    access_token_request_uri_data = requests.get(access_token_request_uri) #uri주소를 데이터형태로 변환한다.
    json_data = access_token_request_uri_data.json() #데이터를 json함수를 이용하여 딕셔너리 형태로 변환한다.
    access_token = json_data['access_token'] #accsee_token값을 가져오고 변수에 대입한다.

    print(access_token)

    #가져온 access_token으로 프로필 정보를 가져온다.
    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
    user_profile_info_uri += str(access_token)
    #프로필정보가 담긴 데이터 가져오기
    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    #프로필정보 중 이름과 프사를 파싱.
    nickName = user_json_data['properties']['nickname']
    profileImageURL = user_json_data['properties']['profile_image']
    thumbnailURL = user_json_data['properties']['thumbnail_image']

    print("nickName = " + str(nickName))
    print("profileImageURL = " + str(profileImageURL))
    print("thumbnailURL = " + str(thumbnailURL))

    template_dict_data = str({
        "object_type": "feed",
        "content": {
            "title": nickName,
            "description": content,
            "image_url": profileImageURL,
            "image_width": 640,
            "image_height": 640,
            "link": {
                "web_url": "http://www.daum.net",
                "mobile_web_url": "http://m.daum.net",
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
        },
        "social": {
            "like_count": 100,
            "comment_count": 200,
            "shared_count": 300,
            "view_count": 400,
            "subscriber_count": 500
        },
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net"
                }
            },
            {
                "title": "앱으로 이동",
                "link": {
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            }
        ]
    })
    #요청할 url
    kakao_to_me_uri = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    headers = {
        'Content-Type': "application/x-www-form-urlencoded", #"template_object="와 같이 '키=값'형태로 전달할 때 쓰는 Content-Type이다.
        'Authorization': "Bearer " + access_token,
    }

    template_json_data = "template_object=" + str(json.dumps(template_dict_data)) #json.dumps(template_dict_data) : 딕셔너리를 json으로 변환
    template_json_data = template_json_data.replace("\"", "") #키값을 감싸고 있는 형태를 json에 맞게 바꿔준다.
    template_json_data = template_json_data.replace("'", "\"") #마찬가지로 json의 형태로 데이터를 가공하는 것.

    response = requests.request(method="POST", url=kakao_to_me_uri, data=template_json_data, headers=headers)
    print(response.json())

    return redirect('blogMain')
