from django.db import models
from .Utils.Errors import Error


# Create your models here.

from django.contrib.auth.models import User   

class Patient(models.Model):
    name = models.CharField(max_length=200, null= True)
    mail = models.EmailField(null = False, unique = True) 
    pwd= models.CharField(null = False)#password
    pseudo = models.CharField(null = False, unique = True)
    phone = models.CharField(max_length = 15)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    errors = {}
    PAGE_TITLE = 'Patient'
    APP_NAME = 'patient'
    
    """
        SETTINGS 
    """
    class Meta:
        verbose_name = ('Patient')
        verbose_name_plural = ('Patients')

    def get_page_title(self):
        return self.PAGE_TITLE

    def get_app_name(self):
        return self.APP_NAME

    """
        INPUT CONTROL 
    """

    

    def input_control_singIn(self, name, mail, pwd, pseudo, phone, age):
        self.errors.clear()
        name = self.set_name(name)
        mail_valid = self.set_mail(mail)
        pwd_valid = self.set_pwd(pwd)
        pwd_c = self.set_pwd_c(pwd_c)
        pseudo_valid = self.set_pseudo(pseudo)
        phone_valid = self.set_phone(phone)
        age_valid = self.set_age(age)

        return (name and 
                mail_valid and 
                pwd_valid and
                pseudo_valid and
                phone_valid and
                age_valid)
    
    """
        SETTER
    """

        
    def set_name(self, name):
        self.name = name
        if not self.name:
            self.errors[Error.NAME] = 'Name is empty'
            return False
        return True
    
    def set_mail(self, mail):
        self.mail = mail
        if not self.mail:
            self.errors[Error.DESC] = 'Mail is empty'
            return False
        return True
    
    def set_pwd(self, pwd):
        self.pwd = pwd
        if not self.pwd:
            self.errors[Error.PWD] = 'Password is empty'
            return False
        return True
    
    def set_pwd_c(self, pwd_c):
        self.pwd_c = pwd_c
        if not self.pwd_c == self.pwd:
            self.errors[Error.PWD_C] = 'Password and confirmation not equals'
            return False
        return True
    
    def set_pseudo(self, pseudo):
        self.pseudo = pseudo
        if not self.pseudo:
            self.errors[Error.PSEUDO] = 'Pseudo is empty'
            return False
        return True
    
    def set_phone(self, phone):
        self.phone = phone
        if not self.phone:
            self.errors[Error.PHONE] = 'Phone is empty'
            return False
        return True
    
    def set_age(self, age):
        self.age = age
        if self.age > 100:
            self.errors[Error.AGE] = "100 ans est l'age maximal"
            return False
        elif self.age < 10:
            self.errors[Error.AGE] = "10 ans est l'age minimal"
        return True
        

    """
        GETTER
    """
    def get_name(self):
        return self.name
    
    def get_mail(self):
        return self.mail
    
    def get_pwd(self):
        return self.pwd
    
    def get_pwd_c(self):
        return self.pwd_c
    
    def get_pseudo(self):
        return self.pseudo

    def get_phone(self):
        return self.phone
    
    def get_age(self):
        return self.age

    def get_errors(self):
        return self.errors
    
    def __str__(self) -> str:
        return self.name
    

#---------------------------------------------------------------------------------------------------------------

class Medecine(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField() 
    online = models.BooleanField(default=False)
    slug = models.SlugField(null = False)
    img = models.ImageField(upload_to='media/', blank = True, null = True)
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
    

        

