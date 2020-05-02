#model에서 데이터베이스를 설계할 수 있다.
from django.db import models
from django.contrib.auth.models import User #장고에서 기본적으로 제공하는 User모델

#from ckeditor.fields import RichTextField #ckeditor에서 텍스트 편집UI를 불러온다.
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model): #import된 models.Model을 매개변수로 받는다.
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True) #현재 시간에 맞추어 입력됨.
    author = models.ForeignKey(User, on_delete=True, null=True, default=1) #User에 있는 계정정보를 쓰겠다.
    body = RichTextUploadingField() #ckeditor_uploader를 적용

#모델 작성 후 python manage.py makemigrations와 migrate를 할 것.
#admin페이지에서 봐야하므로 admin.py에서 모델을 가져오는 코드 작성.

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=True, null=True) #블로그 글마다 있는 주키를 참조하여 몇 번 글에 어떤 댓글을 달지 정한다.
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField()
