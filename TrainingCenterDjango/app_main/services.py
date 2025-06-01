from .forms import groupsForm

def testservice(request):
    form = groupsForm(request.POST)
    if form.is_valid():
        form.save()
    return "отправка удалась"