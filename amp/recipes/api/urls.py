from django.urls import path
from . import views



urlpatterns = [

    path('recipes/', views.get_all_recipes),
    path('recipes/<int:recipe_id>/', views.get_recipe_by_id),
    path('update-fav-recipe/<int:id>/', views.post_fav),
    path('create-recipe/', views.create_recipe),
    path('cuisine_styles/', views.get_styles),
    path('units/', views.get_units),
    path('food_items/', views.get_food_items),
    path('difficulty/', views.get_difficulty),
    

]