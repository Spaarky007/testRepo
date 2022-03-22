from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.sign,name='sign'),
    path('new/',views.hai,name='mine'),

]