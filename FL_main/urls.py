from django.conf.urls import url, include
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'FL_main'

urlpatterns = [
    path('', views.FL_main, name='FL_main'),
]
