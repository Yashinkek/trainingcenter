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
#    form = authorization_form(request.POST)
#    if form.is_valid():
        #all_values = form.cleaned_data
        #user = users.objects.filter(login=all_values.get('login')).first()
        #if user and all_values.get('password') == user.password:
        #    rule = all_values.get('title')
        #    return "авторизация удалась"




#def add_students_group_services(request):
#    form = views_students_form(request.POST)
#    if form.is_valid():
#        ids_student = form.cleaned_data['selected_ids']
#        return "сервис сработал"
