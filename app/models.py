from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100,primary_key=True)


class Coures(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    coures=models.CharField(max_length=100)

class Accessmode(models.Model):
    coures=models.ForeignKey(Coures, on_delete=models.CASCADE)
    free=models.BooleanField(default=True)

