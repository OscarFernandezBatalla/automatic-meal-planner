# from curses.ascii import HT
# from django.http import JsonResponse
from django.http import HttpResponse
# from recipes.forms import RecipeForm
import json
# from recipes.models import Room
# from .serializers import RoomSerializer

from recipes.models import Recipe, CuisineStyle, Unit, Ingredient, FoodItem, Difficulty, Quantity
from recipes.api.serializers import RecipeSerializer, CuisineStyleSerializer, UnitSerializer, FoodItemSerializer, \
    DifficultySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.api import serializers


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


@api_view(['GET'])
def get_recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_styles(request):
    cuisine_styles = CuisineStyle.objects.all()
    serializer = CuisineStyleSerializer(cuisine_styles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_units(request):
    units = Unit.objects.all()
    serializer = UnitSerializer(units, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_food_items(request):
    ingredients = FoodItem.objects.all()
    serializer = FoodItemSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_difficulty_levels(request):
    difficulties = Difficulty.objects.all()
    serializer = DifficultySerializer(difficulties, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_recipe(request):
    # form = RecipeForm()

    # TODO: create is_valid method ¿?

    if request.method == 'POST':
        data = request.POST
        ingredients_list = json.loads(data.get('ingredients'))

        # TODO: change the create of the recipe -> cuisine style, difficulty, etc...

        recipe = Recipe.objects.create(
            name=data.get('name'),
            image=request.FILES.get('image'),
            dinners=data.get('dinners'),

            difficulty=Difficulty.objects.filter(name=data.get('difficulty')).first(),
            cuisine_style=CuisineStyle.objects.filter(name=data.get('cuisine_style')).first(),
            time=data.get('time'),

        )

        for key, value in ingredients_list.items():
            ingredient = json.loads(value)
            food_item = ingredient['food_item']
            quantity = ingredient['quantity']
            unit = ingredient['unit']

            unit_db, unit_created = Unit.objects.get_or_create(name=unit)
            quantity_db, quantity_created = Quantity.objects.get_or_create(value=quantity, unit=unit_db)
            food_item_db, food_item_created = FoodItem.objects.get_or_create(name=food_item)
            ingredient_db, ingredient_created = Ingredient.objects.get_or_create(food_item=food_item_db,
                                                                                 quantity=quantity_db)
            recipe.ingredients.add(ingredient_db)

    return HttpResponse(request.FILES)

    # name = request.POST.get('name'),
    #         image = request.POST.get('image'),
    #         dinners = request.POST.get('dinners'),
    #         difficulty = request.POST.get('difficulty'),
    #         cuisine_style = request.POST.get('cuisine_style'),

    #         fav = request.POST.get('fav'),
    #         time = request.POST.get('time'),

    # {
    #             name: this.name,
    #             image: this.image,
    #             dinners: this.dinners,
    #             difficulty: this.difficulty,
    #             cuisine_style: this.cuisine_style,
    #             ingredinets: this.ingredinets,
    #             fav: this.fav,
    #             time: this.time,
    #         }
