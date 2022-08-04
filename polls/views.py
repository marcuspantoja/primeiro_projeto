#from .models import Choice
from rest_framework import viewsets
#from serializer import ChoiseSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from polls.serializer import ChoiseSerializer
from polls.models import Poll


# ViewSet
class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = Poll.objects.all()
    serializer_class = ChoiseSerializer


# api_view
@api_view(['GET', 'POST'])
def member_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        members = Poll.objects.all()
        serializer = ChoiseSerializer(members, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChoiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)