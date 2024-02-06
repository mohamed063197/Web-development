from django.db import models
from patient.models import Patient
from Utils.Errors import Error


# Create your models here.

from django.contrib.auth.models import User   

#---------------------------------------------------------------------------------------------------------------

class Medecine(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField() 
    online = models.BooleanField(default=False)
    slug = models.SlugField(null = False)
    img = models.ImageField(upload_to='', blank = True, null = True)
    patients = models.ManyToManyField(Patient, related_name='medecines', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    errors = {}
    db_errors = {}
    PAGE_TITLE = 'Medecine'
    APP_NAME = 'medecine'
    
    class Meta:
        verbose_name = ('Medecine')
        verbose_name_plural = ('Medecines')


    """
        SETTINGS 
    """
    def get_page_title(self):
        return self.PAGE_TITLE

    def get_app_name(self):
        return self.APP_NAME

    """
        INPUT CONTROL 
    """    
    def input_control(self, title, desc, online, slug, img):
        self.errors.clear()
        title_valid = self.set_title(title)
        desc_valid = self.set_desc(desc)
        online_valid = self.set_online(online)
        slug_valid = self.set_slug(slug)
        img_valid = self.set_img(img)
        return (title_valid and 
                desc_valid and 
                online_valid and 
                slug_valid and 
                img_valid)
    
    def db_input_control(self, type='add'):
        db_title_valid = self.db_set_title(type=type)
        return (db_title_valid)
    
    def db_set_title(self, type):
        self.db_errors.clear()
        count = Medecine.objects.filter(title__iexact = self.title).count()
        if not((count == 0 and type == 'add') or (count <= 1 and type == 'update')):
            self.db_errors[Error.TITLE] = "Title already exist" 
            return False
        return True
    
    def get_errors_dict(self):
        return {key.value: value for key, value in self.errors.items()}
    
    def get_db_errors_dict(self):
        return {key.value: value for key, value in self.db_errors.items()}
    
    """
        SETTER
    """
    def set_title(self, title):
        self.title = title
        if not self.title:
            self.errors[Error.TITLE] = 'Title is empty'
            return False
        return True

    def set_desc(self, desc):
        self.desc = desc
        if not self.desc:
            self.errors[Error.DESC] = 'Description is empty'
            return False
        return True
    
    def set_online(self, online):
        self.online = online
        return True
    
    def set_slug(self, slug):
        self.slug = slug
        if not self.slug:
            self.errors[Error.SLUG] = 'Slug is empty'
            return False
        return True
    
    def set_img(self, img):
        self.img = img
        return True

    """
        GETTER
    """

    def get_title(self):
        return self.title
    
    
    def get_desc(self):
        return self.desc
    
    def get_online(self):
        return self.online
    
    def get_slug(self):
        return self.slug
    
    def get_img(self):
        return self.img
    
    def get_errors(self):
        return self.errors
    
    def __str__(self) -> str:
        return self.title
    

        

