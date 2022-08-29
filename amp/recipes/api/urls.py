from django.urls import path
from . import views

urlpatterns = [

    path('recipes/', views.get_all_recipes),
    path('recipes/<int:recipe_id>/', views.get_recipe_by_id),
    path('update-fav-recipe/<str:id>/', views.post_fav)
    

]