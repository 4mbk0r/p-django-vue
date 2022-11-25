from secrets import choice
from statistics import mode
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
import jsonfield


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    my_default_errors = {
        'required': 'Se requiere completar datos',
        'invalid': 'Data invalido',
        'unique': 'Nick ya se tiene registrado',
        'blank': 'Se requiere completar datos',
    }
    username = models.CharField(
        max_length=255, unique=True, error_messages=my_default_errors)
    email = models.EmailField('Correo Electrónico',
                              max_length=255, blank=True, null=True)
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)
    last_name = models.CharField(
        'Apellidos', max_length=255, blank=True, null=True)

    bith_date = models.DateField(
        'Fecha_nacimiento', null=True, blank=True)

    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otros', 'Otros'),
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, null=True, blank=True)

    institution = models.CharField(max_length=255, null=True, blank=True)

    image = models.ImageField(
        'Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()
    respuesta = jsonfield.JSONField()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def __getitem__(self, key):
        return self.__dict__[key]
