from rest_framework import serializers
from .models import post_data, recipeTable

class post_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = post_data
        fields = ['id', 'calories', 'height', 'weight', 'name', 'dailyExtraConsume', 'specialDiet', 'age']

class recipeTable_serializer(serializers.ModelSerializer):
    class Meta:
        model = recipeTable
        fields = ['user', 'totalCal', 'foodItem1', 'cal1', 'foodItem2', 'cal2', 'foodItem3', 'cal3', 'foodItem4', 'cal4', 'foodItem5', 'cal5']