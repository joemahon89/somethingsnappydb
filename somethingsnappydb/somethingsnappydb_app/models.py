from django.db import models

# Create your models here.

class Patient (models.Model):
    patient_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()

class Sample (models.Model):
    pass