from django.db import models

# Create your models here.
class Formations(models.Model):
    code = models.CharField(max_length=20)
    libelle = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.libelle