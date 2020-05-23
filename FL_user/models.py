from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username,password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserInfo(AbstractBaseUser):
	HobbyType = (
		(0,"선택하기"),
		(1,"영화보기"),
		(2,"게임"),
		(3,"맛집 탐방"),
		(4,"운동"),
		(5,"음악 감상"),
	)
	BodyType = (
		(0,"선택하기"),
		(1,"마름"),
		(2,"보통"),
		(3,"통통"),
	)
	user_id = models.AutoField(max_length=6, primary_key=True)
	username = models.CharField("아이디",max_length=30,unique=True) #아래에 USERNAME_FIELD를 해줄려면 unique옵션이 필요하다.
	password = models.CharField("비밀번호",default=0,max_length=100)
	name = models.CharField("이름",max_length=30)
	stdnum = models.IntegerField("학번",default=0)
	age = models.IntegerField("나이",default=0)
	hobby = models.IntegerField("취미",default=0,choices=HobbyType)
	height = models.IntegerField("키",default=0)
	weight = models.IntegerField("체형",default=0,choices=BodyType)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_approval = models.BooleanField(default=False)
	objects = UserManager()
	USERNAME_FIELD = 'username'

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
	    return True

	@property
	def is_staff(self):
	    return self.is_admin
