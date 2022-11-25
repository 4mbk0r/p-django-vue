from django.urls import path
#from apps.users.api.api import UserAPIView

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<str:pk>', user_detail_view, name='usuario_detail_api')
]
