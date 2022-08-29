from django.http import JsonResponse
from django.http import HttpResponse
#from recipes.models import Room
#from .serializers import RoomSerializer
from recipes.models import Recipe
from recipes.api.serializers import RecipeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.api import serializers


# TODO: exemple:
"""
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data) 
"""


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_fav(request, id):

    if request.method == 'POST':
        recipe = Recipe.objects.get(pk=id)
        recipe.fav = not recipe.fav
        recipe.save()

    return HttpResponse('Correct')
