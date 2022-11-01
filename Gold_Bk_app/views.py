from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from Gold_Bk_app.serializer import *
# Create your views here.

class Activo_View(viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = Activo_Serializer

class Cuenta_View(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = Cuenta_Serializer

class Trade_View(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = Trade_Serializer

class Usuario_View(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if (token):
            token.delete()
            token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_Serializer(user)
        return Response(usuario.data)
