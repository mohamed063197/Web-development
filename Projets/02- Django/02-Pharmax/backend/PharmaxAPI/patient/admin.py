from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Patient

class PatientInline(admin.StackedInline):
    model = Patient
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (PatientInline, )

# Enregistrez votre CustomUserAdmin avec le modèle User
admin.site.register(User, CustomUserAdmin)