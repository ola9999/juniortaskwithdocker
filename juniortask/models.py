from django.conf import settings
from django.db import models

class Author(models.Model):
    first_name 				= models.CharField(max_length=30, unique=False)
    last_name 				= models.CharField(max_length=30, unique=True)
    date_birth			    = models.DateField( verbose_name ="birthday",  null=True,blank=True, default="1999-11-12" )   

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Note(models.Model):
    author                   = models.ForeignKey(Author, on_delete=models.CASCADE)
    content                    = models.TextField(blank=True, null=True)

    def __str__(self):
       return "author :"+ str(self.author.full_name) + " ,  Note : " + str(self.content)