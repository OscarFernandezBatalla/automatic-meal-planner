from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(CuisineStyle)
admin.site.register(Ingredient)
admin.site.register(Quantity)
admin.site.register(FoodItem)
admin.site.register(Unit)
admin.site.register(Difficulty)
admin.site.register(Step)