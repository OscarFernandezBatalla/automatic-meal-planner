from django.urls import path
from . import views

urlpatterns = [
    #TODO: exemple:
    #path('rooms/', views.getRooms)
    path('recipes/', views.get_all_recipes)
]