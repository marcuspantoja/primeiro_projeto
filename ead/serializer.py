from ead.models import Edital
from rest_framework import serializers



#Create a member serializer
class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        fields = ['id','nome']

'''
class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'        

class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        fields = '__all__'        

'''