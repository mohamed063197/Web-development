from django.contrib import admin
from .models import Medecine
 
# Register your models here.
class AdminMedecine(admin.ModelAdmin):#columns to display for medecine
    list_display = ('title', 'desc', 'online', 'slug', 'img')


admin.site.register(Medecine, AdminMedecine)
