from dataclasses import fields
from polls.models import Poll
from django.contrib.auth.models import User
from rest_framework import serializers

#Create a member serializer
class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'