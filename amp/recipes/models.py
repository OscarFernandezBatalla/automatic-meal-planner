from django.db import models

# Create your models here.


class CuisineStyle(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Quantity(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Recipe(models.Model):
    DIFFICULTY = (
        (1, 'Muy fácil'),
        (2, 'Fácil'),
        (3, 'Media'),
        (4, 'Difícil'),
        (5, 'Muy difícil')
    )

    name = models.CharField(max_length=30, primary_key=True)
    dinners = models.IntegerField()
    difficulty = models.IntegerField(choices=DIFFICULTY)
    cuisine_style = models.ForeignKey(CuisineStyle, on_delete=models.CASCADE) # one recipe has only ONE cuisine_style, but a cuisine_style can be in MANY recipes.
    ingredients = models.ManyToManyField(Ingredient) # one recipe has MANY ingredients, but an ingredient can be in MANY recipes.

