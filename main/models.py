from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = models.CharField(max_length = 50, primary_key=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class post_data(models.Model):
    id = models.CharField(max_length = 50, primary_key= True)
    calories = models.FloatField(default= 2000.0)
    height = models.FloatField(default = 180)
    weight = models.FloatField(default = 75)
    name = models.CharField(max_length=50, default='')
    dailyExtraConsume = models.FloatField(default=0)
    specialDiet = models.CharField(max_length = 100, default = 'none')
    age = models.IntegerField(null = True)


    def __str__(self) :
        return self.name


class foodTable(models.Model):
    foodId = models.IntegerField(primary_key=True)
    foodCal = models.FloatField()
    foodName = models.CharField(max_length = 125)
    trait = models.CharField(max_length = 30)
    restrict = models.CharField(max_length = 30, null = True)
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()

    def __str__(self) :
        return self.foodName
    class Meta:
       indexes = [
           models.Index(fields=['foodCal']),
           models.Index(fields=['foodCal','trait', 'restrict']),
        ]

class recipeTable(models.Model):
    user = models.CharField(max_length = 50, default = '')
    totalCal = models.FloatField(default = 0)
    foodItem1 = models.CharField(max_length=125, null=True)
    cal1 = models.FloatField(default=0)
    foodItem2 = models.CharField(max_length=125, null=True)
    cal2 = models.FloatField(default=0)
    foodItem3 = models.CharField(max_length=125, null=True)
    cal3 = models.FloatField(default=0)
    foodItem4 = models.CharField(max_length=125, null=True)
    cal4 = models.FloatField(default=0)
    foodItem5 = models.CharField(max_length=125, null=True)
    cal5 = models.FloatField(default=0)
    def __str__(self) :
        return self.user
    class Meta:
        indexes = [
           models.Index(fields=['user']),
        ]

