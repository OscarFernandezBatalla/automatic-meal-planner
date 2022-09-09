from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CuisineStyle(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class FoodItem(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Unit(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Quantity(models.Model):
    value = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class Ingredient(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)


class Step(models.Model):
    order = models.IntegerField()
    text = models.CharField(max_length=250)


class Difficulty(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField()


class Recipe(models.Model):
    name = models.CharField(max_length=30, null=True)
    image = models.ImageField(null=True, default="arroz.jpg")
    dinners = models.IntegerField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    cuisine_style = models.ForeignKey(CuisineStyle, on_delete=models.CASCADE) # one recipe has only ONE cuisine_style, but a cuisine_style can be in MANY recipes.
    ingredients = models.ManyToManyField(Ingredient) # one recipe has MANY ingredients, but an ingredient can be in MANY recipes.
    time = models.IntegerField()
    steps = models.ManyToManyField(Step)


    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    liked_recipes = models.ManyToManyField(Recipe, related_name="liked_recipes")
    own_recipes = models.ManyToManyField(Recipe, related_name="own_recipes") # maybe not
    storage = models.ManyToManyField(Ingredient, related_name="storage")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
