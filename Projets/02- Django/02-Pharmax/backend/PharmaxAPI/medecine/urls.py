from django.urls import path
from .views import index, api, update, add, delete, details
app_name='medecine'
urlpatterns = [
    path('api/', api, name="api"),
    path('', index, name = "index"),
    
    path('add/', add, name="add"),

    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('details/<int:id>/', details, name="details"),

]