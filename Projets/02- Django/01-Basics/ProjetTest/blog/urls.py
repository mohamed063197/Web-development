from django.contrib import admin
from django.urls import path
from . import views #depuis le package courant importe views

urlpatterns = [
    #views.home : appele la fonction home qui est dans le modules views
    path("", views.index, name = "index"),
    path("details/<int:id_url>/", views.details, name = 'details'),
]

