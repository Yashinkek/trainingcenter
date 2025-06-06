from .models import students, groups, organizations, users, logs, group_composition
from django.forms import ModelForm
from django import forms


class create_groups_form(ModelForm):
    class Meta:
        model = groups
        fields = ["responsible_person", "status", "direction"]

class delete_groups_form(forms.Form):
    id = forms.IntegerField(label='Group ID')

class authorization_form(ModelForm):
    class Meta:
        model = users
        fields = ["login", "password", "title"]

class views_students_form(forms.Form):
    class Meta:
        model = students
        fields = ["first_name", "last_name", "surname", "passport_number", "date_of_birth", "address_birth", "address", "snils", "education", "passport_issued", "organization", "medical_certificate"]

    selected_ids = forms.ModelMultipleChoiceField(
        queryset=students.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Выберите обучающихся"
    )