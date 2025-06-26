from django.shortcuts import render
from .models import students, groups, organizations, users, logs, group_composition
#from .forms import create_groups_form, authorization_form, views_students_form, delete_groups_form
from .services import create_group_service, authorizationservice, add_students_group_services, delete_group_service
from . import forms
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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
    groups_list = groups.objects.all()

    # Фильтрация
    status = request.GET.get('status')
    direction = request.GET.get('direction')
    responsible_person = request.GET.get('responsible_person')
    group_id = request.GET.get('group_id')

    if status:
        groups_list = groups_list.filter(status__icontains=status)
    if direction:
        groups_list = groups_list.filter(direction__icontains=direction)
    if responsible_person:
        groups_list = groups_list.filter(responsible_person__icontains=responsible_person)
    if group_id:
        groups_list = groups_list.filter(id__icontains=group_id)

    # Пагинация
    paginator = Paginator(groups_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_main/registration_groups.html', {
        'groups': page_obj,
    })
@require_POST
def delete_group(request):
    group_id = request.POST.get('group_id')
    try:
        group = groups.objects.get(id=group_id)
        group.delete()
        return JsonResponse({'success': True})
    except groups.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Group not found'})


@require_POST
def edit_group(request):
    group_id = request.POST.get('group_id')
    status = request.POST.get('status')
    direction = request.POST.get('direction')
    responsible_person = request.POST.get('responsible_person')

    try:
        group = groups.objects.get(id=group_id)
        if status: group.status = status
        if direction: group.direction = direction
        if responsible_person: group.responsible_person = responsible_person
        group.save()
        return JsonResponse({
            'success': True,
            'data': {
                'id': group.id,
                'status': group.status,
                'direction': group.direction,
                'responsible_person': group.responsible_person
            }
        })
    except groups.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Group not found'})
@require_POST
def add_group(request):
    try:
        new_group = groups(
            status=request.POST.get('status'),
            direction=request.POST.get('direction'),
            responsible_person=request.POST.get('responsible_person')
        )
        new_group.save()
        return JsonResponse({'success': True, 'group_id': new_group.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})




def registration_students(request):
    students_list = students.objects.all()

    # Фильтрация
    student_id = request.GET.get('student_id')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    surname = request.GET.get('surname')
    passport_number = request.GET.get('passport_number')
    date_of_birth = request.GET.get('date_of_birth')
    address_birth = request.GET.get('address_birth')
    address = request.GET.get('address')
    snils = request.GET.get('snils')
    education = request.GET.get('education')
    passport_issued = request.GET.get('passport_issued')
    organization = request.GET.get('organization')
    medical_certificate = request.GET.get('medical_certificate')


    if first_name:
        students_list = students_list.filter(first_name__icontains=first_name)
    if last_name:
        students_list = students_list.filter(last_name__icontains=last_name)
    if surname:
        students_list = students_list.filter(surname__icontains=surname)
    if passport_number:
        students_list = students_list.filter(passport_number__icontains=passport_number)
    if date_of_birth:
        students_list = students_list.filter(date_of_birth__icontains=date_of_birth)
    if address_birth:
        students_list = students_list.filter(address_birth__icontains=address_birth)
    if address:
        students_list = students_list.filter(address__icontains=address)
    if snils:
        students_list = students_list.filter(snils__icontains=snils)
    if education:
        students_list = students_list.filter(education__icontains=education)
    if passport_issued:
        students_list = students_list.filter(passport_issued__icontains=passport_issued)
    if organization:
        students_list = students_list.filter(organization__icontains=organization)
    if medical_certificate:
        students_list = students_list.filter(medical_certificate__icontains=medical_certificate)
    if student_id:
        students_list = students_list.filter(id__icontains=student_id)

    # Пагинация
    paginator = Paginator(students_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_main/registration_students.html', {
        'students': page_obj,
    })

@require_POST
def delete_student(request):
    student_id = request.POST.get('student_id')  # Исправлено с group_id на student_id
    try:
        student = students.objects.get(id=student_id)
        student.delete()
        return JsonResponse({'success': True})
    except students.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Student not found'})


@require_POST
def edit_student(request):
    student_id = request.POST.get('student_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    surname = request.POST.get('surname')
    passport_number = request.POST.get('passport_number')
    date_of_birth = request.POST.get('date_of_birth')
    address_birth = request.POST.get('address_birth')
    address = request.POST.get('address')
    snils = request.POST.get('snils')
    education = request.POST.get('education')
    passport_issued = request.POST.get('passport_issued')
    organization = request.POST.get('organization')
    medical_certificate = request.POST.get('medical_certificate')

    try:
        student = students.objects.get(id=student_id)
        if first_name: student.first_name = first_name
        if last_name: student.last_name = last_name
        if surname: student.surname = surname
        if passport_number: student.passport_number = passport_number
        if date_of_birth: student.date_of_birth = date_of_birth
        if address_birth: student.address_birth = address_birth
        if address: student.address = address
        if snils: student.snils = snils
        if education: student.education = education
        if passport_issued: student.passport_issued = passport_issued
        if organization: student.organization = organization
        if medical_certificate: student.medical_certificate = medical_certificate
        student.save()
        return JsonResponse({
            'success': True,
            'data': {
                'id': student.id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'surname': student.surname,
                'passport_number': student.passport_number,
                'date_of_birth': student.date_of_birth,
                'address_birth': student.address_birth,
                'address': student.address,
                'snils': student.snils,
                'education': student.education,
                'passport_issued': student.passport_issued,
                'organization': student.organization,
                'medical_certificate': student.medical_certificate
            }
        })
    except students.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Student not found'})
@require_POST
def add_student(request):
    try:
        new_student = students(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            surname=request.POST.get('surname'),
            passport_number=request.POST.get('passport_number'),
            date_of_birth=request.POST.get('date_of_birth'),
            address_birth=request.POST.get('address_birth'),
            address=request.POST.get('address'),
            snils=request.POST.get('snils'),
            education=request.POST.get('education'),
            passport_issued=request.POST.get('passport_issued'),
            organization=request.POST.get('organization'),
            medical_certificate=request.POST.get('medical_certificate')
        )
        new_student.save()
        return JsonResponse({'success': True, 'student_id': new_student.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})






def registration_organizations(request):
    orgs_list = organizations.objects.all()

    # Фильтрация
    name = request.GET.get('name')
    ogrn = request.GET.get('ogrn')
    inn = request.GET.get('inn')
    kpp = request.GET.get('kpp')

    if name:
        orgs_list = orgs_list.filter(name__icontains=name)
    if ogrn:
        orgs_list = orgs_list.filter(ogrn__icontains=ogrn)
    if inn:
        orgs_list = orgs_list.filter(inn__icontains=inn)
    if kpp:
        orgs_list = orgs_list.filter(kpp__icontains=kpp)

    # Пагинация
    paginator = Paginator(orgs_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_main/registration_organizations.html', {
        'organizations': page_obj,
    })

@require_POST
def delete_organization(request):
    org_id = request.POST.get('org_id')
    try:
        org = organizations.objects.get(id=org_id)
        org.delete()
        return JsonResponse({'success': True})
    except organizations.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Organization not found'})

@require_POST
def edit_organization(request):
    org_id = request.POST.get('org_id')
    name = request.POST.get('name')
    ogrn = request.POST.get('ogrn')
    inn = request.POST.get('inn')
    kpp = request.POST.get('kpp')

    try:
        org = organizations.objects.get(id=org_id)
        if name: org.name = name
        if ogrn: org.ogrn = ogrn
        if inn: org.inn = inn
        if kpp: org.kpp = kpp
        org.save()
        return JsonResponse({
            'success': True,
            'data': {
                'id': org.id,
                'name': org.name,
                'ogrn': org.ogrn,
                'inn': org.inn,
                'kpp': org.kpp
            }
        })
    except organizations.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Organization not found'})

@require_POST
def add_organization(request):
    try:
        new_org = organizations(
            name=request.POST.get('name'),
            ogrn=request.POST.get('ogrn'),
            inn=request.POST.get('inn'),
            kpp=request.POST.get('kpp')
        )
        new_org.save()
        return JsonResponse({'success': True, 'org_id': new_org.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def registration(request):
    form1 = forms.registration_groups_form()
    form2 = forms.registration_students_form()
    g = groups.objects.all()
    context = {
        'form1': form1,
        'form2': form2,
        'groups': g
    }
    return render(request, 'app_main/registration.html', context)

def monitoring(request):
    return render(request, 'app_main/monitoring.html')

def print(request):
    students_list = students.objects.all()

    # Фильтрация
    student_id = request.GET.get('student_id')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    surname = request.GET.get('surname')
    passport_number = request.GET.get('passport_number')
    date_of_birth = request.GET.get('date_of_birth')
    address_birth = request.GET.get('address_birth')
    address = request.GET.get('address')
    snils = request.GET.get('snils')
    education = request.GET.get('education')
    passport_issued = request.GET.get('passport_issued')
    organization = request.GET.get('organization')
    medical_certificate = request.GET.get('medical_certificate')

    if first_name:
        students_list = students_list.filter(first_name__icontains=first_name)
    if last_name:
        students_list = students_list.filter(last_name__icontains=last_name)
    if surname:
        students_list = students_list.filter(surname__icontains=surname)
    if passport_number:
        students_list = students_list.filter(passport_number__icontains=passport_number)
    if date_of_birth:
        students_list = students_list.filter(date_of_birth__icontains=date_of_birth)
    if address_birth:
        students_list = students_list.filter(address_birth__icontains=address_birth)
    if address:
        students_list = students_list.filter(address__icontains=address)
    if snils:
        students_list = students_list.filter(snils__icontains=snils)
    if education:
        students_list = students_list.filter(education__icontains=education)
    if passport_issued:
        students_list = students_list.filter(passport_issued__icontains=passport_issued)
    if organization:
        students_list = students_list.filter(organization__icontains=organization)
    if medical_certificate:
        students_list = students_list.filter(medical_certificate__icontains=medical_certificate)
    if student_id:
        students_list = students_list.filter(id__icontains=student_id)

    # Пагинация
    paginator = Paginator(students_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_main/print.html', {
        'students': page_obj,
    })