from .models import students, groups, organizations, users, logs, group_composition
from django.forms import ModelForm


class groupsForm(ModelForm):
    class Meta:
        model = groups
        fields = ["responsible_person", "status", "direction" ]