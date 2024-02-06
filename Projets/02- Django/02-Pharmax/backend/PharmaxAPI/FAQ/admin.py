from django.contrib import admin
from .models import FAQ
 
# Register your models here.
class AdminFAQ(admin.ModelAdmin):#columns to display for FAQ
    list_display = ('title', 'desc', 'desc_sound', 'online', 'slug','medecine')  

admin.site.register(FAQ, AdminFAQ)