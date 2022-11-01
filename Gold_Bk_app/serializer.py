from rest_framework import serializers
from Gold_Bk_app.models import *

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            direccion=validated_data['direccion'],
            telefono=validated_data['telefono'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Activo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Activo
        fields = '__all__'

class Cuenta_Serializer(serializers.ModelSerializer):
    usuario = Usuario_Serializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Usuario.objects.all(), source='usuario')

    class Meta:
        model = Cuenta
        fields = '__all__'

class Trade_Serializer(serializers.ModelSerializer):
    cuenta = Cuenta_Serializer(read_only=True)
    id_cuenta = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cuenta.objects.all(), source='cuenta')
    activo = Activo_Serializer(read_only=True)
    id_activo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Activo.objects.all(), source='activo')

    class Meta:
        model = Trade
        fields = '__all__'

