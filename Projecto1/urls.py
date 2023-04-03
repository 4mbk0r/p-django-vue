"""Projecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    path('admin/', admin.site.urls),
    path('inicio/', login_inicio, name='inicio'),
    path('registro/',registar, name='registro'),
    path('bienvenido/',bienvenido, name='bienvenido'),
    path('logout/',cerrar_login, name='logout'),
    path('',index, name=''),
    path('salachat/',chatbot, name='salachat'),
    path('quiz/',quiz, name='quiz'),
    path('test', vue_views.test_vue), 
    path('new/', test_new, name='new'),
    path('api/v1.0/', include('book.urls')) """


from apps.users.views import Login, Logout
from apps.quizz.views import Pregunta, chatGPT
from xml.etree.ElementInclude import include
from Projecto1.views import bienvenido, login_inicio, registar,  cerrar_login, index, chatbot, quiz, test_new, suma
from django.contrib import admin
from django.contrib.auth import login, logout
from django.urls import path, include
from django.conf.urls import url
# from vue_app import views as vue_views  # This line is new
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pregunta/', Pregunta.as_view(), name="pregunta"),
    url('porapi/', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.book.urls')),
    path('users/', include('apps.users.api.routers')),
    path('login/', Login.as_view(), name="Login"),
    path('logout/', Logout.as_view(), name="Logout"),
    path('add/', suma, name="adicionar"),
    url('respuesta/',  chatGPT.as_view(), name="respuesta   "),
    url('', TemplateView.as_view(template_name='index.html')),


]
