from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    file_pdf = models.FileField(upload_to='files/')
    formation_id = models.ForeignKey('formations.Formations', on_delete=models.CASCADE)
    prof_id = models.ForeignKey('prof.Prof', on_delete=models.CASCADE)   