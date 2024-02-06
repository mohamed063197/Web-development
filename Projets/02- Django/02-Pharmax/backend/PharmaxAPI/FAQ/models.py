from django.db import models
from medecine.models import Medecine
from Utils.Errors import Error 

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=150, null= False)
    desc = models.TextField(null = False) 
    desc_sound = models.FileField(upload_to='sounds/', blank = True, null = True)
    online = models.BooleanField(default=False)
    slug = models.SlugField(null = False, default='slug')
    medecine = models.ForeignKey(Medecine, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    errors = {}
    db_errors = {}
    PAGE_TITLE = 'FAQ'
    APP_NAME = 'FAQ'
    
    class Meta:
        verbose_name = ('FAQ')
        verbose_name_plural = ('FAQs')

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
    def input_control(self, title, desc,online, slug, medecine, desc_sound):
        self.errors.clear()
        title_valid = self.set_title(title)
        desc_valid = self.set_desc(desc)
        online_valid = self.set_online(online)
        slug_valid = self.set_slug(slug)
        medecine_valid = self.set_medecine(medecine)
        desc_sound_valid = self.set_desc_sound(desc_sound)
        return title_valid and desc_valid and desc_sound_valid and online_valid and slug_valid and medecine_valid
    
    def db_input_control(self, type='add', medecine = None):
        db_title_valid = self.db_set_title(type=type)
        #db_medecine_valid = self.db_set_medecine(medecine = medecine)
        return (db_title_valid)
    
    def db_set_title(self, type):
        self.db_errors.clear()
        count = FAQ.objects.filter(title__iexact = self.title).count()
        if not((count == 0 and type == 'add') or (count <= 1 and type == 'update')):
            self.db_errors[Error.TITLE] = "Title already exist" 
            return False
        return True
    
    def db_set_medecine(self, type):
        
        return True
    
    def get_errors_dict(self):
        return {key.value: value for key, value in self.errors.items()}
    
    def get_db_errors_dict(self):
        return {key.value: value for key, value in self.db_errors.items()}
    
    """
        SETTER
    """   
    def set_title(self, ntitle):
        self.title = ntitle
        if not self.title:
            self.errors[Error.TITLE] = 'Title is empty'
            return False
        return True
    
    def set_desc(self, ndesc):
        self.desc = ndesc
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
    
    def set_medecine(self, medecine):
        self.medecine = medecine
        if not self.medecine:
            #self.errors[Error.MEDECINE] = 'Medecine is empty'
            return False
        return True
    
    def set_desc_sound(self, ndesc_sound):
        self.desc_sound = ndesc_sound
        if not self.desc_sound:
            self.errors[Error.DESC_SOUND] = 'Description sound is empty'
            return False
        return True

    """
        GETTER
    """
    def get_title(self):
        return self.title
    
    def get_medecine(self):
        return self.medecine
    
    def get_desc(self):
        return self.desc
    
    def get_online(self):
        return self.online
    
    def get_slug(self):
        return self.slug
    
    def get_desc_sound(self):
        return self.desc_sound

    def get_errors(self):
        return self.errors
    
    def get_medecine(self):
        return self.medecine
    
    def __str__(self) -> str:
        return self.title
