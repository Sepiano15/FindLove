from django.contrib import admin
from .models import Blog #Blog모델을 가져온다. 모델 작성 후 할 것.
from .models import Comment
# Register your models here.
admin.site.register(Blog) #Blog모델을 등록.
admin.site.register(Comment)
#모델 등록 후 관리자페이지가 아니라 메인 화면에서 하려면 forms.py를 만들어서 작성.
