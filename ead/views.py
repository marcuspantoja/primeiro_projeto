#from .models import Choice
from rest_framework import viewsets
from rest_framework import serializers
#from serializer import ChoiseSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ead.serializer import EditalSerializer
from ead.models import  Edital



# ViewSet
'''
class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = DadosPessoais.objects.all()
    serializer_class = ChoiseSerializer


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
'''

class EditalViewSet(viewsets.ModelViewSet):
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer    


    
'''
# api_view
@api_view(['GET', 'POST'])
def member_api(request, nome):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        members = DadosPessoais.objects.filter(nome=nome)
        serializer = ChoiseSerializer(members, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChoiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def carro_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        carros = Carro.objects.all()
        serializer = CarroSerializer(carros, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
'''
@api_view(['GET', 'POST'])
def edital_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        editais = Edital.objects.all()
        print("editais", editais)
        serializer = EditalSerializer(editais, many=True)
        print(serializer)
        print(serializer.data)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EditalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            