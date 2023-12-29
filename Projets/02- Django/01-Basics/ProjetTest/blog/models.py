from django.db import models

class TimeCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


# Create your models here.
class Post(TimeCreatedModel):
    title = models.CharField(max_length=255, default="No Title")
    content = models.TextField(default="No Content")
 
"""
    #Constructeur Alternatif
    @classmethod
    def fromString(cls, s="TitreParDefaut-ContentParDefaut"):
        data = s.split('-')
        return cls(title = data[0], content = data[1])

    @classmethod
    def getNumberOfPosts(cls):
        return cls.number_of_posts

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def getByTitle(cls, _title):
        return cls.objects.get(title = t)

    @classmethod
    def getById(cls, _id):
        return cls.objects.get(id = _id)

    def __str__(self):
        return f'Post [ Title : {title} ,Content : {content} ]'
"""