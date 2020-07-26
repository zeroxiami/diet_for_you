from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import post_data, foodTable, recipeTable
from django.db import connection, transaction
import random

# Create your views here.
def test(request):
   person = post_data.objects.raw('SELECT * FROM main_post_data')
   return render(request, 'test2.html', {'info' : person}
   )

def edit(request, person_id):
   thisPerson = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [person_id])
   for p in thisPerson:
         person = p

   return render(request, 'test.html', {'info':person})
   

def post_info(request):
   personId = request.POST['pid']
   newName = request.POST['name']
   newCal = request.POST['cal']
   newWeight = request.POST['weight']
   newHeight = request.POST['height']
   with connection.cursor() as cursor:
      cursor.execute("UPDATE main_post_data SET name = %s, calories = %s, weight = %s, height = %s WHERE id = %s", [newName, newCal, newWeight, newHeight, personId])   
   return redirect('/main/')

def recipe(request):
   recipeInfo = recipeTable.objects.raw('SELECT * FROM main_recipeTable')
   return render(request, 'recipe.html', {'recipeInfo' : recipeInfo})

def recipeDelete(request, recipeId):
   with connection.cursor() as cursor:
      cursor.execute("DELETE FROM main_recipeTable WHERE id = %s", [recipeId])
   return redirect('/recipe/')

def recipeAdd(request):
   rangeFood = 6
   a = random.randint(1, 6)
   b = random.randint(1, 6)
   c = random.randint(1, 6)
   food1q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodId = %s', [a])
   for p in food1q:
      food1 = p
   food2q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodId = %s', [b])
   for p in food2q:
      food2 = p
   food3q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodId = %s', [a])
   for p in food3q:
      food3 = p
   inserts = recipeTable(foodItem1 = food1.foodName, cal1 = food1.foodCal, foodItem2 = food2.foodName, 
   cal2 = food2.foodCal, foodItem3 = food3.foodName, cal3 = food3.foodCal)
   inserts.save()
   return redirect('/recipe/')
