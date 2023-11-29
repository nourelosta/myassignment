from django.db import models

# Create your models here.
class Contact(models.Model):
 name = models.CharField(max_length=100)
 address = models.CharField(max_length=200)
 profession = models.CharField(max_length=100)
 telnumber = models.CharField(max_length=15)
 email = models.EmailField()

 def __str__(self):
  return self.name