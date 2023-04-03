from dataclasses import fields
from apps.quizz.models import PreguntaModel
from rest_framework import serializers


#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PreguntarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaModel
        fields = '__all__'

