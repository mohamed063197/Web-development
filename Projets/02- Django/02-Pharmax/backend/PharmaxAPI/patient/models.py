from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    """    name = models.CharField(max_length=200, null= True)
    mail = models.EmailField(null = False, unique = True) 
    pwd= models.CharField(null = False)
    pseudo = models.CharField(null = False, unique = True)
    """

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