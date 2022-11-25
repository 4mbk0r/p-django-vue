from django.db import models
import jsonfield
# Create your models here.


class quiz(models.Model):
    my_default_errors = {
        'required': 'Se requiere completar datos',
        'invalid': 'Data invalido',
        'unique': 'Nick ya se tiene registrado',
        'blank': 'Se requiere completar datos',
    }
    username = models.CharField(
        max_length=255, default="", primary_key=True, unique=True, error_messages=my_default_errors)
    preguntas = jsonfield.JSONField()
