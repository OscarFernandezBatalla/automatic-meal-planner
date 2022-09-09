from pyexpat import model
from django.forms import ModelForm
from .models import Recipe



class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        #__all__ to make form of all 
        fields = '__all__'

