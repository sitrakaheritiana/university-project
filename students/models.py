from django.db import models

# Create your models here.
class Student(models.Model):
    matricule = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)