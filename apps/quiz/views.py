from django.shortcuts import render

# Create your views here.
from apps.quiz.api.serializer import PreguntarSerializer


class Preguntas(GenericAPIView):
    serializer_class = PreguntarSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
