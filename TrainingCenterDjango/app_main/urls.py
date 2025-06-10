from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create_group', views.create_group, name='create_group'),
    path('authorization', views.authorization, name='authorization'),
    path('add_students_group', views.add_students_group, name='add_students_group'),
    path('delete_group', views.delete_group, name='delete_group')
]
