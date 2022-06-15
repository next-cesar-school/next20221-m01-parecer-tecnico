from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Exemplo, Cliente


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ExemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplo
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'