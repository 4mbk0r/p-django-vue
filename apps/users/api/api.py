
from email import message
from pyexpat import model
from rest_framework.response import Response
from rest_framework import viewsets
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.models import User
from apps.users.api.serializer import UserSerializer, UserListSerializer, RegistrationSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.core import serializers


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    model = User
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        users = self.get_queryset()

        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        user_serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if user_serializer.is_valid():
            password = request.data.get('password', '')
            user_serializer.save()
            login_serializer_class = CustomTokenObtainPairSerializer
            login_serializer = login_serializer_class(
                data=request.data, context={'request': request})
            username = request.data.get('username', '')

            print(username, password)
            user = authenticate(
                username=username,
                password=password
            )
            print(user)
            if user:
                if login_serializer.is_valid():
                    access = login_serializer.validated_data.get('access')
                    refresh = login_serializer.validated_data.get('refresh')
                    return Response({
                        'token': access,
                        'refresh-token': refresh,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesion Existoso'
                    }, status=status.HTTP_200_OK)
            return Response({'message': 'Usuario registro correctamente'}, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay un error en los datos',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


"""
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serizalizer = UserSerializer(users,many=True)
        return Response(users_serizalizer.data)
"""

"""

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serizalizer = UserSerializer(users,many=True)
        return Response(users_serizalizer.data)
    if request.method == 'POST':
        user_serizalizer = UserSerializer(data = request.data)
        if user_serizalizer.is_valid():
            user_serizalizer.save()
            return Response(user_serizalizer.data)
        return Response(user_serizalizer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request,pk):
    
    user =  User.objects.filter(username=pk).first()
    if user:
        if request.method == 'GET':
        
            user_serializar =  UserSerializer(user)
            return Response(user_serializar.data)
        elif request.method == 'PUT':
            user =  User.objects.filter(username=pk).first()
            user_serializer =  UserSerializer(user, data= request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializar.errors)
        elif request.method == 'DELETE':
            user =  User.objects.filter(username=pk).first()
            user.delete()
            return Response('Eliminado')
    else:
        return Response({'message': 'No se encontro el usario'}, status = status.HTTP_400_BAD_REQUEST)
"""
