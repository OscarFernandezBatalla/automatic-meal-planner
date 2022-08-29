from django.http import JsonResponse
#from recipes.models import Room
#from .serializers import RoomSerializer
from recipes.models import Recipe
from recipes.api.serializers import RecipeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.api import serializers


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)
