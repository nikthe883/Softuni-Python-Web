from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("dashboard", views.dashboard, name="dashboard"),
   path("profile/create", views.create_profile, name="create_profile"),
   path("profile/details", views.details_profile, name="details_profile"),
   path("profile/edit", views.edit_profile, name="edit_profile"),
   path("profile/delete", views.delete_profile, name="delete_profile"),
]