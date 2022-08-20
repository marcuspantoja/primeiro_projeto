from ead.models import Edital
from rest_framework import serializers



#Create a member serializer
class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        fields = '__all__'
