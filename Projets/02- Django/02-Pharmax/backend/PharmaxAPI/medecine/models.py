from django.db import models

# Create your models here.

class Medecine(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField() 
    favorite = models.BooleanField(default=False)
    #desc_sound = models.FileField(upload_to='sons/', blank = True, null = True)
    slug = models.SlugField(null = True)
    img = models.ImageField(upload_to='imgs/', blank = True, null = True)
    #relier a une table qui contient FAQ

    
    
    class Meta:
        verbose_name = ('Medecine')
        verbose_name_plural = ('Medecines')

    def get_favorite(self):
        return self.favorite
    
    def __str__(self) -> str:
        return self.title
        
    