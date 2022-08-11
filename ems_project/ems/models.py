from re import T
from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    Gender_Choice = [('M', 'Male'), ('F', 'Feale'), ('0', 'Other')]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=14, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=Gender_Choice)
    dob = models.DateField()
    joining_date = models.DateField()
    jobs = models.ManyToManyField('Job', blank=True)

class Job(models.Model):
        name = models.CharField(max_length=250)
        
        def __str__(self):
            return self.name