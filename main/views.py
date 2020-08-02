from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import post_data, foodTable, recipeTable, SignUpForm
from django.db import connection, transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import random
from rest_framework import viewsets
from .serializers import post_data_serializer, recipeTable_serializer

class post_data_view(viewsets.ModelViewSet):
   serializer_class = post_data_serializer
   queryset = post_data.objects.all()

class recipeTable_view(viewsets.ModelViewSet):
   serializer_class = recipeTable_serializer
   queryset = recipeTable.objects.all()

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
   currentUser = request.user
   personId = currentUser.username
   recipeInfo = recipeTable.objects.raw('SELECT * FROM main_recipeTable WHERE user = %s', [personId])
   return render(request, 'recipe.html', {'recipeInfo' : recipeInfo})

def recipeDelete(request, recipeId):
   with connection.cursor() as cursor:
      cursor.execute("DELETE FROM main_recipeTable WHERE id = %s", [recipeId])
   return redirect('/recipe/')

def recipeAdd(request):
   currentUser = request.user
   personId = currentUser.username
   thisPerson = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [personId])
   for p in thisPerson:
         person = p
   totalCal = float(person.calories)+float(person.dailyExtraConsume)
   if person.specialDiet == 'none':
      food1q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal <= %s AND restrict = %s ORDER BY random() LIMIT 1', [totalCal/2, 'Breakfast'])
      for p in food1q:
         food1 = p
         cal1 = 2*float(food1.foodCal)
         totalCal = totalCal - cal1
      food2q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal < %s AND restrict <> %s ORDER BY random() LIMIT 1', [totalCal/1.5, 'Breakfast'])
      for p in food2q:
         food2 = p
         cal2 = 1.5*float(food2.foodCal)
         totalCal = totalCal - cal2
      food3q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', [totalCal/6, totalCal/4, 'Breakfast'])
      for p in food3q:
         food3 = p
         cal3 = 2*float(food3.foodCal)
         totalCal = totalCal - cal3
      food4q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', [totalCal/5, totalCal/3, 'Breakfast'])
      for p in food4q:
         food4 = p
         cal4 = 1.5*float(food4.foodCal)
         totalCal = totalCal - cal4
      food5q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', [totalCal/2, totalCal/1.5, 'Breakfast'])
      for p in food5q:
         food5 = p
         cal5 = 1.5*float(food5.foodCal) 
      total = cal1 + cal2 + cal3 + cal4 + cal5  
      inserts = recipeTable(user = personId, totalCal = total, foodItem1 = food1.foodName, cal1 = cal1, foodItem2 = food2.foodName, 
         cal2 = cal2, foodItem3 = food3.foodName, cal3 = food3.foodCal, foodItem4 = food4.foodName, cal4 = cal4, 
         foodItem5 = food5.foodName, cal5 = cal5)
      inserts.save()
      return redirect('/recipe/')
   elif person.specialDiet == 'vegetarian':
      food1q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal <= %s AND restrict = %s ORDER BY random() LIMIT 1', ['Meat', totalCal/2, 'Breakfast'])
      for p in food1q:
         food1 = p
         cal1 = 2*float(food1.foodCal)
         totalCal = totalCal - cal1
      food2q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal < %s AND restrict <> %s ORDER BY random() LIMIT 1', ['Meat', totalCal/1.5, 'Breakfast'])
      for p in food2q:
         food2 = p
         cal2 = 1.5*float(food2.foodCal)
         totalCal = totalCal - cal2
      food3q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['Meat', totalCal/6, totalCal/4, 'Breakfast'])
      for p in food3q:
         food3 = p
         cal3 = 2*float(food3.foodCal)
         totalCal = totalCal - cal3
      food4q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['Meat', totalCal/5, totalCal/3, 'Breakfast'])
      for p in food4q:
         food4 = p
         cal4 = 1.5*float(food4.foodCal)
         totalCal = totalCal - cal4
      food5q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['Meat', totalCal/2, totalCal/1.5, 'Breakfast'])
      for p in food5q:
         food5 = p
         cal5 = 1.5*float(food5.foodCal) 
      total = cal1 + cal2 + cal3 + cal4 + cal5  
      inserts = recipeTable(user = personId, totalCal = total, foodItem1 = food1.foodName, cal1 = cal1, foodItem2 = food2.foodName, 
         cal2 = cal2, foodItem3 = food3.foodName, cal3 = food3.foodCal, foodItem4 = food4.foodName, cal4 = cal4, 
         foodItem5 = food5.foodName, cal5 = cal5)
      inserts.save()
      return redirect('/recipe/')
