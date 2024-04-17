from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/catalogue/', views.recipe_catalogue, name='recipe_catalogue'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_id>/details/', views.recipe_details, name='recipe_details'),
    path('recipe/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
]
