from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserInfo
from .forms import UserChangeForm, UserCreationForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'user_id', 'name', 'age','hobby','stdnum','is_admin','is_approval')
    list_filter = ('is_approval','hobby')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin','is_approval')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','name','stdnum','age','hobby','height','weight')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(UserInfo, UserAdmin)
admin.site.unregister(Group)
#모델 등록 후 관리자페이지가 아니라 메인 화면에서 하려면 forms.py를 만들어서 작성.
