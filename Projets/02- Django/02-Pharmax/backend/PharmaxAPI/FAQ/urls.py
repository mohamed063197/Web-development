from django.urls import path
from .views import index, api, update, add, delete, details
app_name='FAQ'
urlpatterns = [
    path('api/<int:m>/', api, name="api"),
    path('<int:m>/', index, name = "index"),

    path('add/<int:m>/', add, name="add"),

    path('update/<int:m>/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('details/<int:m>/<int:id>/', details, name="details"),

]