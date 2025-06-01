from django.contrib import admin
from .models import students, groups, organizations, users, logs, group_composition
# Register your models here.

admin.site.register(students)
admin.site.register(groups)
admin.site.register(organizations)
admin.site.register(users)
admin.site.register(logs)
admin.site.register(group_composition)