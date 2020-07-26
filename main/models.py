from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class post_data(models.Model):
    id = models.IntegerField(primary_key= True)
    calories = models.FloatField(default= 2000.0)
    height = models.FloatField(default = 180)
    weight = models.FloatField(default = 75)
    name = models.CharField(max_length=50, default='')
    dailyExtraConsume = models.FloatField(default=0)
    specialDiet = models.CharField(max_length = 100, default = 'none')
    age = models.IntegerField(null = True)
    dateOfJoin = models.DateField(auto_now_add= True, null =True)


    def __str__(self) :
        return self.name


class foodTable(models.Model):
    foodId = models.IntegerField(primary_key=True)
    foodCal = models.FloatField()
    foodName = models.CharField(max_length = 125)
    trait = models.CharField(max_length = 30)
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()

    def __str__(self) :
        return self.foodName

class recipeTable(models.Model):
    foodItem1 = models.CharField(max_length=125, null=True)
    cal1 = models.FloatField(default=0)
    foodItem2 = models.CharField(max_length=125, null=True)
    cal2 = models.FloatField(default=0)
    foodItem3 = models.CharField(max_length=125, null=True)
    cal3 = models.FloatField(default=0)

