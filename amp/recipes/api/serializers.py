from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer
#from recipes.models import Room
from recipes.models import Recipe
#TODO: exemple
"""
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
"""


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
        
