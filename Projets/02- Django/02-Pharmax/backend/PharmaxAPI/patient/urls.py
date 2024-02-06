from django.urls import path
from .views import apiRegister, apiLogin, apiLogout

app_name='patient'
urlpatterns = [
    path('apiRegister/', apiRegister, name="apiRegister"),
    path('apiLogin/', apiLogin, name="apiLogin"),
    path('apiLogout/', apiLogout, name="apiLogout"),
]