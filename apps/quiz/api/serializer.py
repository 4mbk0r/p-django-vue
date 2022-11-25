from dataclasses import fields
from apps.quiz.models import quiz
from apps.users.models import User
from rest_framework import serializers

#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PreguntarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
