from django.db import models

# Create your models here.
class User(models.Model):
    user_rules = {
        'admin': 'admin',
        'prof': 'prof',
        'student': 'student',
    }
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100, choices=user_rules)
    