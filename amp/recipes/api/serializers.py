from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer, SerializerMethodField
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

    image_url = SerializerMethodField('get_image')

    class Meta:
        model = Recipe
        #fields = "__all__"

        

        fields = (
            'name',
            'image_url',
            'dinners',
            'difficulty',
            'cuisine_style',
            'ingredients'
        )

    def get_image(self, object):
            if object.image:
                return 'http://127.0.0.1:8000' + object.image.url


        
        
