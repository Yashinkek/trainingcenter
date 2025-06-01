from django.shortcuts import render
from .models import students, groups, organizations, users, logs, group_composition
from .forms import groupsForm
from .services import testservice
list = [1, "asxasx", "12345 newcom"]
def index(request):
    g = groups.objects.all()
    return render(request, 'app_main/index.html', {'groups': g})

def about(request):
    return render(request, 'app_main/about.html')

def create(request):
    t = ""
    if request.method == 'POST':
        t = testservice(request)
    form = groupsForm()

    context = {
        'form' : form,
        't' : t
    }
    return render(request, 'app_main/create.html', context)