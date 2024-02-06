from django.db import models
from django.contrib.auth.models import User
from Utils.Errors import Error 

# Create your models here.
class Patient(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 15)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    errors = {}
    db_errors = {}
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
    def input_control_singIn(self, name, username, mail, pwd, phone, age):
        self.errors.clear()
        name = self.set_name(name)
        username = self.set_username(username)
        mail_valid = self.set_mail(mail)
        pwd_valid = self.set_pwd(pwd)
        pwd_c = self.set_pwd_c(pwd_c)
        phone_valid = self.set_phone(phone)
        age_valid = self.set_age(age)

        return (name and 
                username and
                mail_valid and 
                pwd_valid and
                phone_valid and
                age_valid)
    
    def db_input_control_singIn(self, type='add'):
        db_mail_valid = self.db_set_mail(type=type)
        db_username_valid = self.db_set_username(type=type)
        return (db_mail_valid and
                db_username_valid)
    
    def db_set_mail(self, type):
        self.db_errors.clear()
        count = self.account.objects.filter(mail__iexact = self.account.email).count()
        if not((count == 0 and type == 'add') or (count <= 1 and type == 'update')):
            self.db_errors[Error.MAIL] = "Mail already exist" 
            return False
        return True
    
    def db_set_username(self, type):
        self.db_errors.clear()
        count = self.account.objects.filter(username__iexact = self.account.username).count()
        if not((count == 0 and type == 'add') or (count <= 1 and type == 'update')):
            self.db_errors[Error.USERNAME] = "Username already exist" 
            return False
        return True
    
    def get_errors_dict(self):
        return {key.value: value for key, value in self.errors.items()}
    
    def get_db_errors_dict(self):
        return {key.value: value for key, value in self.db_errors.items()}
    
    """
        SAVE
    """
    def save(self):
        if not self.user.pk:
            self.user.save()
        super(Patient, self).save()
    """
        SETTER
    """
    def set_name(self, name):
        self.account.last_name = name
        if not self.account.last_name:
            self.errors[Error.NAME] = 'Name is empty'
            return False
        return True
    
    def set_username(self, username):
        self.account.username = username
        if not self.account.username:
            self.errors[Error.USERNAME] = 'Username is empty'
            return False
        return True
    
    
    def set_mail(self, mail):
        self.account.email = mail
        if not self.account.email:
            self.errors[Error.DESC] = 'Mail is empty'
            return False
        return True
    
    def set_pwd(self, pwd):
        self.account.password = pwd
        if not self.account.password:
            self.errors[Error.PWD] = 'Password is empty'
            return False
        return True
    
    def set_pwd_c(self, pwd_c):
        self.pwd_c = pwd_c
        if not self.pwd_c == self.pwd:
            self.errors[Error.PWD_C] = 'Password and confirmation not equals'
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
        return self.account.last_name
    
    def get_username(self):
        return self.account.username
    
    def get_mail(self):
        return self.account.email
    
    def get_pwd(self):
        return self.account.password
    
    def get_pwd_c(self):
        return self.pwd_c


    def get_phone(self):
        return self.phone
    
    def get_age(self):
        return self.age

    def get_errors(self):
        return self.errors
    
    def __str__(self) -> str:
        return self.name