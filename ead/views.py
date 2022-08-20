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


    


@api_view(['GET'])
def get_edital_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        editais = Edital.objects.all()
        serializer = EditalSerializer(editais, many=True)
        return Response(serializer.data)

    

@api_view(['POST'])
def post_edital_api(request, nome):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    edital = Edital()
    edital.nome = nome
    if request.method == 'POST':
        serializer = EditalSerializer(data={"nome":edital.nome})
        print("serializer", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                 