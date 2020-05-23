from django import forms #장고에서 지원하는 forms를 import
from .models import UserInfo
from ckeditor_uploader.widgets import CKEditorUploadingWidget #글쓰는 부분(body)을 꾸미기 위해 import한다.
from django.contrib import auth
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=12,widget=forms.PasswordInput,required=True)
    #password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())

    class Meta:
        model = UserInfo
        fields = ['username', 'password','name','stdnum','age','hobby','height','weight']

    # def InsertUsername(self,user): #사용자가 중복확인을 완료했을 때 호출된다. form의 아이디에 사용자가 적은 값을 넣는다.
    #     self.Meta.fields[0]=user #중복확인 버튼을 눌러도 입력한 아이디가 사라지지 않는다.

    # def InsertPassword(self,password): 
    #     self.Meta.fields[1]=password

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=12,widget=forms.PasswordInput,required=True)

    class Meta:
        model = UserInfo
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ('username', 'password','name','stdnum','age','hobby','height','weight')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'is_approval', 'is_admin')

    def clean_password(self):
        return self.initial["password"]