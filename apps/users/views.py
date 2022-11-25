

from datetime import datetime
from traceback import print_tb
#from urllib.request import Request
#from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token
#from rest_framework import permissions, status
from apps.users.api.serializer import (
    UserLoginSerializer, CustomTokenObtainPairSerializer)
#from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token
from django.http import JsonResponse
# from braces.views import CsrfExemptMixin
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print(username, password)
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(
                data=request.data, context={'request': request})
            if login_serializer.is_valid():
                user_serializer = UserLoginSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    serializer_class = CustomTokenObtainPairSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        name = request.data.get('name', '')
        user = User.objects.filter(username=name)
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)


"""username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(
                data=request.data, context={'request': request})
            if login_serializer.is_valid():
                user = login_serializer.validated_data['user']
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    print(token, created)
                    user_serializer = UserLoginSerializer(user)
                    if created:
                        return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'creted': created,
                            'message': 'Bienvenido'},
                            status=status.HTTP_200_OK)
                    else:
                        token.delete()
                        token = Token.objects.create(user=user)
                        return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'message': 'Ya tienes session'},
                            status=status.HTTP_200_OK)

                else:
                    return Response({'error': 'Este usuario no esta login'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'datos incorretos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message: hola desde response'}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={request})
        if login_serializer.is_valid():
            # user = login_serializer.validated_data['user']
            return Response({'message: hola desde response aaa'}, status=status.HTTP_200_OK)"""

"""
class Logout(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        #try:
            print('nuevoooosooos')
            print(request.data)
            token = request.data.get('token', '')
            name = request.data.get('name', '')

            token = Token.objects.filter(key=token).first()

            if token:
                print(name)
                user = User.objects.filter(username=name)
                if user.exists():
                    #RefreshToken.for_user(user.first())
                    token.delete()
                    return Response({'message: Session finalizada'}, status=status.HTTP_200_OK)
                return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)
        #except:
            return Response({'error': 'No se encntrado token'}, status=status.HTTP_409_CONFLICT)
"""
