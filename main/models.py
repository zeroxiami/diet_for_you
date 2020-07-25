from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class post_data(models.Model):
    id = models.IntegerField(primary_key= True)
    calories = models.FloatField(default= 2000.0)
    height = models.FloatField(default = 180)
    weight = models.FloatField(default = 75)
    name = models.CharField(max_length=50, default='')

    def __str__(self) :
        return self.name