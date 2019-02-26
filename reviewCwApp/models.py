from django.db import models

# Create your models here.
#Create a cocktail Model with name, alcohol percentage, and serving glass.

class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    alcohol_percentage = models.IntegerField()
    serving_glass = models.IntegerField()