from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create_group', views.create_group, name='create_group'),
    path('authorization', views.authorization, name='authorization'),
    path('add_students_group', views.add_students_group, name='add_students_group'),
    path('registration_groups', views.registration_groups, name='registration_groups'),
    path('delete_group/', views.delete_group, name='delete_group'),
    path('edit_group/', views.edit_group, name='edit_group'),
    path('add_group/', views.add_group, name='add_group'),
    path('monitoring', views.monitoring, name='monitoring'),
    path('print', views.print, name='print'),
path('export-student-to-pdf/', views.export_student_to_pdf, name='export_student_to_pdf'),
path('print/students/', views.export_student_to_pdf, name='print_students'),
    path('registration_students', views.registration_students, name='registration_students'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('edit_student/', views.edit_student, name='edit_student'),
    path('add_student/', views.add_student, name='add_student'),
    path('registration_organizations', views.registration_organizations, name='registration_organizations'),
    path('delete_organization/', views.delete_organization, name='delete_organization'),
    path('edit_organization/', views.edit_organization, name='edit_organization'),
    path('add_organization/', views.add_organization, name='add_organization'),
    path('registration', views.registration, name='registration'),
]
