from django.db import models

# Create your models here.

class Applicants(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)

