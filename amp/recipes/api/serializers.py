from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from recipes.models import Recipe, CuisineStyle, Unit, FoodItem
#TODO: exemple
"""
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
"""

class DifficultySerializer(ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('DIFFICULTY',)

class CuisineStyleSerializer(ModelSerializer):
    
    class Meta:
        model = CuisineStyle
        fields = "__all__"

class UnitSerializer(ModelSerializer):
    
    class Meta:
        model = Unit
        fields = "__all__"

class FoodItemSerializer(ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = "__all__"


class RecipeSerializer(ModelSerializer):

    image_url = SerializerMethodField('get_image')

    class Meta:
        model = Recipe
        #fields = "__all__"

        fields = (
            'id',
            'name',
            'image_url',
            'dinners',
            'difficulty',
            'cuisine_style',
            'ingredients',
            'fav',
            'time'
        )

    def get_image(self, object):
        if object.image:
            return 'http://127.0.0.1:8000' + object.image.url


