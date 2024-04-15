from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("dashboard", views.dashboard, name="dashboard"),
   path("profile/create", views.create_profile, name="create_profile"),
   path("profile/create", views.create_profile, name="create_profile"),
]