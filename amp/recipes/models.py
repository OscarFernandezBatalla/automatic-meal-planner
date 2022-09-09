from django.db import models

# Create your models here.


class CuisineStyle(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class FoodItem(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Quantity(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class Ingredient(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)


class Recipe(models.Model):
    DIFFICULTY = (
        (1, 'Muy fácil'),
        (2, 'Fácil'),
        (3, 'Media'),
        (4, 'Difícil'),
        (5, 'Muy difícil')
    )

    name = models.CharField(max_length=30, null=True)
    image = models.ImageField(null=True, default="arroz.jpg")
    dinners = models.IntegerField(null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, null=True)
    cuisine_style = models.ForeignKey(CuisineStyle, on_delete=models.CASCADE, null=True) # one recipe has only ONE cuisine_style, but a cuisine_style can be in MANY recipes.
    ingredients = models.ManyToManyField(Ingredient, null=True) # one recipe has MANY ingredients, but an ingredient can be in MANY recipes.
    fav = models.BooleanField(default=False, null=True)
    time = models.IntegerField(null=True)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
