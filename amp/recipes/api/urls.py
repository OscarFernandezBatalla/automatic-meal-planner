from django.urls import path
from . import views

urlpatterns = [
    #TODO: exemple:
    #path('rooms/', views.getRooms)
    path('recipes/', views.get_all_recipes),
    path('update-fav-recipe/<str:id>/', views.post_fav)
]