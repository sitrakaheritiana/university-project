from django.db import models

# Create your models here.
class Note(models.Model):
    value = models.FloatField()
    student_id = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('cours.Course', on_delete=models.CASCADE)
