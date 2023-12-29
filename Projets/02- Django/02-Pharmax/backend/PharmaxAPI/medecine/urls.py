from django.urls import path
from .views import index, api, update

urlpatterns = [
    path('api/', api, name="api"),
    path('', index, name = "index"),
    path('update/', update, name="update"),
]