from django.db import models

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
    group = models.IntegerField('Группа')
    organization = models.IntegerField('Организация')
    medical_certificate = models.CharField('Медицинская справка', max_length=200)

class groups(models.Model):
    responsible_person = models.IntegerField('Ответственное лицо')
    status = models.CharField('Статус', max_length=200)
    direction = models.CharField('Напрвление', max_length=200)

class organizations(models.Model):
    name = models.CharField('Наименование', max_length=200)
    ogrn = models.CharField('ОГРН', max_length=200)
    inn = models.CharField('ИНН', max_length=200)
    kpp = models.CharField('КПП', max_length=200)

class users(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    surname = models.CharField('Отчество', max_length=200)
    title = models.CharField('Должность', max_length=200)
    login = models.CharField('Логин', max_length=200)
    password = models.CharField('Пароль', max_length=200)

class logs(models.Model):
    table = models.CharField('Таблица', max_length=200)
    operation = models.CharField('Вид операции', max_length=200)
    number = models.IntegerField('id Записи')
    date = models.DateField('Дата')
    user = models.IntegerField('Совершено')

class group_composition(models.Model):
    group = models.IntegerField('Группа')
    student = models.IntegerField('Обучающийся')
