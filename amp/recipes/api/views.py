from django.http import JsonResponse
#from recipes.models import Room
#from .serializers import RoomSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.api import serializers


#TODO: exemple:
"""
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data) 
"""