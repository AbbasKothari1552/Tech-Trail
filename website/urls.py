from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('user_code', views.user_code, name= 'riddle'),
]
