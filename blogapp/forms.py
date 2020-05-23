from django import forms #장고에서 지원하는 forms를 import
from .models import Blog,Comment #Blog model 가져오기.
from ckeditor_uploader.widgets import CKEditorUploadingWidget #글쓰는 부분(body)을 꾸미기 위해 import한다.
from django.contrib.auth.models import User
from django.contrib import auth

class CreateBlog(forms.ModelForm):
    class Meta: #Meta는 내부클래스로서 기본 필드의 값을 정의할 때 사용한다.
        model = Blog

        fields = ['title', 'body'] #Blog 모델에서 정의된 요소 중 가져올 것을 적는다.
        widgets = { #장고에서 제공하는 폼의 형태를 빌려올 수 있다.
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'author': forms.Select(
            #     attrs={'class': 'custom-select'},
            # ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()), #ckeditor의 upoading widget을 적용한 부분이다.
        }
#forms.py 작성 후 이것을 띄워줄 템플릿 html을 만들 것. 위 경우에는 createBlog.html임.
#템플릿 만들면 view에 함수 작성하고 urls.py에 url등록하기.
#그 후 뷰에다가 forms를 import하기.
class BlogCommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ['text']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].label = "댓글"

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }
