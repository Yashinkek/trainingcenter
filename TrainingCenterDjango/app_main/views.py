from django.shortcuts import render
from .models import students, groups, organizations, users, logs, group_composition
#from .forms import create_groups_form, authorization_form, views_students_form, delete_groups_form
from .services import create_group_service, authorizationservice, add_students_group_services, delete_group_service
from . import forms
def index(request):
    g = groups.objects.all()
    return render(request, 'app_main/index.html', {'groups': g})

def about(request):
    return render(request, 'app_main/about.html')

def create_group(request):
    response = ""
    if request.method == 'POST':
        response = create_group_service(request)
    form = forms.create_groups_form()

    context = {
        'form' : form,
        't' : response
    }
    return render(request, 'app_main/create_group.html', context)

def delete_group(request):
    response = ""
    if request.method == 'POST':
        response = delete_group_service(request)
    form = forms.delete_groups_form()

    context = {
        'form' : form,
        'response' : response
    }
    return render(request, 'app_main/delete_group.html', context)


def authorization(request):
    response = ""
    if request.method == 'POST':
        response = authorizationservice(request)
    form = forms.authorization_form()

    context = {
        'form' : form,
        'response' : response
    }
    return render(request, 'app_main/authorization.html', context)

def add_students_group(request):
    response = ""
    if request.method == 'POST':
        response = add_students_group_services(request)

    form = forms.views_students_form()
    s = students.objects.all()
    g = groups.objects.all()
    context = {
        'form' : form,
        'response' : response,
        'students' : s,
        'groups': g
    }
    return render(request, 'app_main/add_students_group.html', context)

def registration_groups(request):
    form = forms.registration_groups_form()
    g = groups.objects.all()
    context = {
        'form': form,
        'groups': g
    }
    return render(request, 'app_main/registration_groups.html', context)
def registration_students(request):
    form = forms.registration_students_form()
    s = students.objects.all()
    context = {
        'form': form,
        'students': s
    }
    return render(request, 'app_main/registration_students.html', context)
def registration_organizations(request):
    form = forms.registration_organizations_form()
    o = organizations.objects.all()
    context = {
        'form': form,
        'organizations': o
    }
    return render(request, 'app_main/registration_organizations.html', context)
def registration_organizations(request):
    return render(request, 'app_main/registration_organizations.html')

def monitoring(request):
    return render(request, 'app_main/monitoring.html')

def print(request):
    return render(request, 'app_main/print.html')