from django.db import models

# Create your models here.


class PreguntaModel(models.Model):
    my_default_errors = {
        'required': 'Se requiere completar datos',
        'invalid': 'Data invalido',
        'unique': 'Nick ya se tiene registrado',
        'blank': 'Se requiere completar datos',
    }
    nro = models.CharField(max_length=255, default="", primary_key=True,
                           unique=True, error_messages=my_default_errors)
    preguntas = models.TextField()
