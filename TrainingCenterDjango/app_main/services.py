from django.shortcuts import redirect
from .forms import create_groups_form, authorization_form, views_students_form, delete_groups_form
from .models import students, groups, organizations, users, logs, group_composition, save_orm, delete_orm
from django.shortcuts import get_object_or_404

def create_group_service(request):
    form = create_groups_form(request.POST)
    if form.is_valid():
        save_orm(form)
        return "сохранение удалась"

def delete_group_service(request):
    form = delete_groups_form(request.POST)
    if form.is_valid():
        delete_orm(form)
        return "Удаление удалось"


#def authorizationservice(request):
#    print("сервис вызван")
#    form = authorization_form(request.POST)
#    if form.is_valid():
#        print("данные валидны")
#        all_values = form.cleaned_data
#        login = all_values.get('login')
#        password = all_values.get('password')
#        user = users.authorization(login, password)
#        #user = users.objects.filter(login=all_values.get('login')).first()
#        if user:
#            print("fdnjhbpfwbz elfkfcm")
#            return "авторизация удалась"


def authorizationservice(request):
    print("сервис вызван")
    form = authorization_form(request.POST)
    if form.is_valid():
        print("данные валидны")
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = users.authorization(login=login, password=password)

        if user:
            print("авторизация удалась")
            return redirect('registration_groups')
        else:
            print("неверные данные для входа")
            # Возвращаем None или False вместо строки
            return None
    else:
        print("данные не валидны")
        # Возвращаем None или False вместо строки
        return None


def add_students_group_services(request):
    form = views_students_form(request.POST)
    if form.is_valid():
        ids_student = form.cleaned_data['selected_ids']
        return "сервис сработал"
