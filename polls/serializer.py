from dataclasses import fields
from termios import CKILL
from polls.models import DadosPessoais, Carro
from django.contrib.auth.models import User
from rest_framework import serializers

#Create a member serializer
class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'        