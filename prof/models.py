from django.db import models

# Create your models here.
class Prof(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)