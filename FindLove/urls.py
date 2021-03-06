"""FindLove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import FL_main.views
import FL_user.views
#미디어 추가를 위한 import
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

#path(1,2,3)인자별 설명
#1 : 접속할 주소. 이 주소에 접속하면 2에있는 일을 하겠다.
#2 : 위에 import blogapp.view를 해서 가능함. view에 있는 index함수를 쓰겠다는 말.
#3 : 함수를 적용시키고 이름을 정하면 나중에 html파일에서 이 값으로 url을 불러올 수 있다.
urlpatterns = [
    path('', FL_main.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('logout/',FL_main.views.logout, name='logout'),
    path('signup/',FL_user.views.signup, name='signup'),
    path('about/',FL_main.views.about, name='about'),
    path('login_cert/',FL_user.views.login_cert, name='login_cert'),
]

#미디어 추가를 위한 경로참조
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('signup/',views.signup, name='signup'),
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('modify_info/',views.modify_info, name='modify_info'),
    path('write_profile/',views.write_profile, name='write_profile'),
    path('show_profile/',views.show_profile, name='show_profile'),
    path('heartlist/',views.heartlist, name='heartlist'),
    path('success/',views.success, name='success'),
    path('blogMain/',views.blogMain, name='blogMain'), #blogMain의 url을 view를 만든 뒤 추가하는 구간.
    path('blogMain/createBlog',views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')), #ckeditor_uploader가 url을 참조할 수 있도록 한다.
    path('blogMain/detail/<int:document_id>/', views.detail, name='detail'),
    path('oauth/', views.oauth, name='oauth'),
'''