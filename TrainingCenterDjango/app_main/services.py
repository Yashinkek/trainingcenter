from .forms import creategroupsForm, authorizationForm, viewsstudentsForm, deletegroupsForm
from .models import students, groups, organizations, users, logs, group_composition
from django.shortcuts import get_object_or_404

def create_group_service(request):
    form = creategroupsForm(request.POST)
    if form.is_valid():
        form.save()
    return "отправка удалась"

def delete_group_service(request):
    form = deletegroupsForm(request.POST)
    if form.is_valid():
        group_id = form.cleaned_data['id']
        group = get_object_or_404(groups, id=group_id)
        group.delete()
        return "Удаление удалось"


def authorizationservice(request):
    form = authorizationForm(request.POST)
    if form.is_valid():
        all_values = form.cleaned_data
        user = users.objects.filter(login=all_values.get('login')).first()
        if user and all_values.get('password') == user.password:
            rule = all_values.get('title')
            return "авторизация удалась"




def add_students_group_services(request):
    form = viewsstudentsForm(request.POST)
    if form.is_valid():
        ids_student = form.cleaned_data['selected_ids']
        return "сервис сработал"
