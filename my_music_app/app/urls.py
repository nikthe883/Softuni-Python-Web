from django.urls import path
from. import views


urlpatterns = [
    path("", views.home, name="home"),

    path("album/add", views.add_album, name='add-album'),

    path("album/details/<str:pk>", views.details_album, name='details-album'),

    path("album/edit/<str:pk>", views.edit_album, name='edit-album'),

    path("album/delete/<str:pk>", views.delete_album, name='delete-album'),

    path("profile/details", views.profile_details, name='profile-details'),

    path("profile/delete", views.profile_delete, name='profile-delete'),

]