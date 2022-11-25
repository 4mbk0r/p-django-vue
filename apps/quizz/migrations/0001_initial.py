# Generated by Django 3.2.5 on 2022-09-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('nro', models.CharField(default='', error_messages={'blank': 'Se requiere completar datos', 'invalid': 'Data invalido', 'required': 'Se requiere completar datos', 'unique': 'Nick ya se tiene registrado'}, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('preguntas', models.TextField()),
            ],
        ),
    ]
