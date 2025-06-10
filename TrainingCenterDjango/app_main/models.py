from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class students(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    surname = models.CharField('Отчество', max_length=200)
    passport_number = models.CharField('Номер паспорта', max_length=200)
    date_of_birth = models.DateField('Дата рождения')
    address_birth = models.CharField('Место рождения', max_length=200)
    address = models.CharField('Адрес', max_length=200)
    snils = models.CharField('СНИЛС', max_length=200)
    education = models.CharField('Документ об образовании', max_length=200)
    passport_issued = models.CharField('Паспорт выдан', max_length=200)
    organization = models.IntegerField('Организация')
    medical_certificate = models.CharField('Медицинская справка', max_length=200)

    def search(cls, query):
        return cls.objects.filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(surname__icontains=query) |
            models.Q(passport_number__icontains=query) |
            models.Q(date_of_birth__icontains=query) |
            models.Q(address_birth__icontains=query) |
            models.Q(address__icontains=query) |
            models.Q(snils__icontains=query) |
            models.Q(education__icontains=query) |
            models.Q(passport_issued__icontains=query) |
            models.Q(organization__icontains=query) |
            models.Q(medical_certificate__icontains=query)
        )

    def update(self, first_name=None, last_name=None, surname=None, passport_number=None, date_of_birth=None , address_birth=None ,address=None, snils=None ,education=None, passport_issued=None ,organization=None, medical_certificate=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if surname:
            self.surname = surname
        if passport_number:
            self.passport_number = passport_number
        if date_of_birth:
            self.date_of_birth = date_of_birth
        if address_birth:
            self.address_birth = address_birth
        if address:
            self.address = address
        if snils:
            self.snils = snils
        if education:
            self.education = education
        if passport_issued:
            self.passport_issued = passport_issued
        if organization:
            self.organization = organization
        if medical_certificate:
            self.medical_certificate = medical_certificate
        self.save()

class groups(models.Model):
    responsible_person = models.IntegerField('Ответственное лицо')
    status = models.CharField('Статус', max_length=200)
    direction = models.CharField('Напрвление', max_length=200)

    def search(cls, query):
        return cls.objects.filter(
            models.Q(responsible_person__icontains=query) |
            models.Q(status__icontains=query) |
            models.Q(direction__icontains=query)
        )

    def update(self, responsible_person=None, status=None, direction=None):
        if responsible_person:
            self.responsible_person = responsible_person
        if status:
            self.status = status
        if direction:
            self.direction = direction
        self.save()

    def update_status(self, status=None):
        if status:
            self.status = status
        else:
            if self.status == "ожидание":
                self.status = "зачислены"
            if self.status == "зачислены":
                self.status = "сдали"
            if self.status == "сдали":
                self.status = "отчислены"

class organizations(models.Model):
    name = models.CharField('Наименование', max_length=200)
    ogrn = models.CharField('ОГРН', max_length=200)
    inn = models.CharField('ИНН', max_length=200)
    kpp = models.CharField('КПП', max_length=200)

    def search(cls, query):
        return cls.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(ogrn__icontains=query) |
            models.Q(inn__icontains=query) |
            models.Q(kpp__icontains=query)
        )

    def update(self, name=None, ogrn=None, inn=None, kpp=None):
        if name:
            self.name = name
        if ogrn:
            self.ogrn = ogrn
        if inn:
            self.inn = inn
        if kpp:
            self.kpp = inn
        self.save()


class users(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    surname = models.CharField('Отчество', max_length=200)
    title = models.CharField('Должность', max_length=200)
    login = models.CharField('Логин', max_length=200)
    password = models.CharField('Пароль', max_length=200)

    def search(cls, query):
        return cls.objects.filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(surname__icontains=query) |
            models.Q(title__icontains=query) |
            models.Q(login__icontains=query) |
            models.Q(password__icontains=query)
        )

    def update(self, first_name=None, last_name=None, surname=None, title=None, login=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if surname:
            self.surname = surname
        if title:
            self.title = title
        if login:
            self.login = login
        if password:
            self.password = password
        self.save()

    def authorization(cls, query):
        return cls.objects.filter(
            models.Q(login__icontains=query) |
            models.Q(password__icontains=query)
        )
    def rule_check(cls, query):
        return cls.objects.filter(
            models.Q(id__icontains=query)
        )

class logs(models.Model):
    table = models.CharField('Таблица', max_length=200)
    operation = models.CharField('Вид операции', max_length=200)
    number = models.IntegerField('id Записи')
    date = models.DateField('Дата')
    user = models.IntegerField('Совершено')

    def search(cls, query):
        return cls.objects.filter(
            models.Q(table__icontains=query) |
            models.Q(operation__icontains=query) |
            models.Q(number__icontains=query) |
            models.Q(date__icontains=query) |
            models.Q(user__icontains=query)
        )

class group_composition(models.Model):
    group = models.IntegerField('Группа')
    student = models.IntegerField('Обучающийся')


def save_orm(form):
    form.save()
    return "save_orm"
def delete_orm(form):
    values_id = form.cleaned_data['id']
    values = get_object_or_404(groups, id=values_id)
    values.delete()