from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import post_data, foodTable, recipeTable, SignUpForm
from django.db import connection, transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import random


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'profile.html', {'userId': username})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
   currentUser = request.user
   personId = currentUser.username
   newName = request.POST['name']
   newCal = request.POST['cal']
   newWeight = request.POST['weight']
   newHeight = request.POST['height']
   exercise = request.POST['exercise']
   diet = request.POST['speicalDiet']
   age = request.POST['age']
   with connection.cursor() as cursor:
      cursor.execute("INSERT INTO main_post_data(id, calories, height, weight, name, dailyExtraConsume, specialDiet, age) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", [personId, newCal, newHeight, newWeight, newName, exercise, diet, age])   
   return redirect('/main/')



def personalInfo(request):
   currentUser = request.user
   personId = currentUser.username
   person = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [personId])    
   return render(request, 'test2.html', {'info' : person}
   )

def edit(request):
   currentUser = request.user
   personId = currentUser.username
   thisPerson = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [personId])
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
