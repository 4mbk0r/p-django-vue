from django.shortcuts import render


#from urllib.request import Request
#from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token
#from rest_framework import permissions, status
from apps.quizz.api.serializer import PreguntarSerializer
#from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token
from django.http import JsonResponse
# from braces.views import CsrfExemptMixin
from apps.quizz.models import PreguntaModel
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class Pregunta(GenericAPIView):
    serializer_class = PreguntarSerializer

    def get_queryset(self):
        return PreguntaModel.objects.all()

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        pregunta = PreguntaModel.objects.all()
        s_pregunta = self.serializer_class(pregunta, many=True)
        if pregunta.exists():
            # RefreshToken.for_user(user.first())
            return Response(s_pregunta.data, status=status.HTTP_200_OK)
        return Response({'error': 'Error an la obtencion.'}, status=status.HTTP_400_BAD_REQUEST)
