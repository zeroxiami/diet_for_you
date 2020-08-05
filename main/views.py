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

def home(request):
    currentUser = request.user
    personId = currentUser.username
    person = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [personId])
    return render(request, "home.html", {'info' : person})



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
   exercise = request.POST['exercise']
   diet = request.POST['speicalDiet']
   age = request.POST['age']
   with connection.cursor() as cursor:
      cursor.execute("UPDATE main_post_data SET name = %s, calories = %s, weight = %s, height = %s, dailyExtraConsume = %s, specialDiet = %s,  age = %s WHERE id = %s", [newName, newCal, newWeight, newHeight, exercise, diet, age, personId])
   return redirect('/main/')

def recipe(request):
   currentUser = request.user
   personId = currentUser.username
   recipeInfo = recipeTable.objects.raw('SELECT * FROM main_recipeTable WHERE user = %s ORDER BY id desc LIMIT 1', [personId])
   if len(recipeInfo) == 0:
      recipeInfo = recipeTable.objects.raw('SELECT * FROM main_recipeTable ORDER BY random() LIMIT 1')
   return render(request, 'recipe.html', {'recipeInfo' : recipeInfo})

def pastRecipe(request):
   currentUser = request.user
   personId = currentUser.username
   recipeInfo = recipeTable.objects.raw('SELECT * FROM main_recipeTable WHERE user = %s ORDER BY id', [personId])
   return render(request, 'past_recipe.html', {'recipeInfo' : recipeInfo})

def recipeDelete(request, recipeId):
   with connection.cursor() as cursor:
      cursor.execute("DELETE FROM main_recipeTable WHERE id = %s", [recipeId])
   return redirect('/recipe/')

def recipeUpdate(request, foodItem, recipeId):
   foodItemq = recipeTable.objects.raw('SELECT * FROM main_recipeTable WHERE id = %s', [recipeId])
   for p in foodItemq:
      foodItems = p
   totalCal = float(foodItems.totalCal)
   currentUser = request.user
   personId = currentUser.username
   thisPerson = post_data.objects.raw('SELECT * FROM main_post_data WHERE id = %s', [personId])
   for p in thisPerson:
         person = p
   if person.specialDiet == 'none':
      if foodItem == 1:
         foodItem = foodItems.foodItem1
         cal = float(foodItems.cal1)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict = %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/3, cal/1.2, 'Breakfast', foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem1 = %s, cal1 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 2:
         foodItem = foodItems.foodItem2
         cal = float(foodItems.cal2)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem2 = %s, cal2 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 3:
         foodItem = foodItems.foodItem3
         cal = float(foodItems.cal3)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2.5, cal/1.2, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem3 = %s, cal3 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 4:
         foodItem = foodItems.foodItem4
         cal = float(foodItems.cal4)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem4 = %s, cal4 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 5:
         foodItem = foodItems.foodItem5
         cal = float(foodItems.cal5)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem5 = %s, cal5 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
   elif person.specialDiet == 'vegetarian':
      if foodItem == 1:
         foodItem = foodItems.foodItem1
         cal = float(foodItems.cal1)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND restrict = %s AND foodName <> %s ORDER BY random() LIMIT 1', ['Meat', cal/3, cal/1.2, 'Breakfast', foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem1 = %s, cal1 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 2:
         foodItem = foodItems.foodItem2
         cal = float(foodItems.cal2)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', ['Meat', cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem2 = %s, cal2 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 3:
         foodItem = foodItems.foodItem3
         cal = float(foodItems.cal3)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', ['Meat', cal/2.5, cal/1.2, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem3 = %s, cal3 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 4:
         foodItem = foodItems.foodItem4
         cal = float(foodItems.cal4)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', ['Meat', cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem4 = %s, cal4 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 5:
         foodItem = foodItems.foodItem5
         cal = float(foodItems.cal5)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', ['Meat', cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem5 = %s, cal5 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
   elif person.specialDiet == 'ketogenic diet':
      if foodItem == 1:
         foodItem = foodItems.foodItem1
         cal = float(foodItems.cal1)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict = %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/3, cal/1.2, 'Breakfast', foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem1 = %s, cal1 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 2:
         foodItem = foodItems.foodItem2
         cal = float(foodItems.cal2)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem2 = %s, cal2 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 3:
         foodItem = foodItems.foodItem3
         cal = float(foodItems.cal3)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2.5, cal/1.2, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 2*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem3 = %s, cal3 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 4:
         foodItem = foodItems.foodItem4
         cal = float(foodItems.cal4)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem4 = %s, cal4 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
      if foodItem == 5:
         foodItem = foodItems.foodItem5
         cal = float(foodItems.cal5)
         newFoodq = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND foodName <> %s ORDER BY random() LIMIT 1', [cal/2, cal/1, foodItem])
         for p in newFoodq:
            newFood = p
         newCal = 1.5*float(newFood.foodCal)
         totalCal = totalCal - cal + newCal
         with connection.cursor() as cursor:
            cursor.execute("UPDATE main_recipeTable SET foodItem5 = %s, cal5 = %s, totalCal = %s WHERE id = %s", [newFood.foodName, newCal, totalCal, recipeId])
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
      food5q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', [totalCal/3.2, totalCal/1.5, 'Breakfast'])
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
      food5q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE trait <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['Meat', totalCal/3.2, totalCal/1.5, 'Breakfast'])
      for p in food5q:
         food5 = p
         cal5 = 1.5*float(food5.foodCal)
      total = cal1 + cal2 + cal3 + cal4 + cal5
      inserts = recipeTable(user = personId, totalCal = total, foodItem1 = food1.foodName, cal1 = cal1, foodItem2 = food2.foodName,
         cal2 = cal2, foodItem3 = food3.foodName, cal3 = food3.foodCal, foodItem4 = food4.foodName, cal4 = cal4,
         foodItem5 = food5.foodName, cal5 = cal5)
      inserts.save()
      return redirect('/recipe/')
   elif person.specialDiet == 'ketogenic diet':
      food1q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE restrict <> %s AND foodCal <= %s AND restrict = %s ORDER BY random() LIMIT 1', ['High Carb', totalCal/2, 'Breakfast'])
      for p in food1q:
         food1 = p
         cal1 = 2*float(food1.foodCal)
         totalCal = totalCal - cal1
      food2q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE restrict <> %s AND foodCal < %s AND restrict <> %s ORDER BY random() LIMIT 1', ['High Carb', totalCal/1.5, 'Breakfast'])
      for p in food2q:
         food2 = p
         cal2 = 1.5*float(food2.foodCal)
         totalCal = totalCal - cal2
      food3q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE restrict <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['High Carb', totalCal/6, totalCal/4, 'Breakfast'])
      for p in food3q:
         food3 = p
         cal3 = 2*float(food3.foodCal)
         totalCal = totalCal - cal3
      food4q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE restrict <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['High Carb', totalCal/5, totalCal/3, 'Breakfast'])
      for p in food4q:
         food4 = p
         cal4 = 1.5*float(food4.foodCal)
         totalCal = totalCal - cal4
      food5q = foodTable.objects.raw('SELECT * FROM main_foodTable WHERE restrict <> %s AND foodCal BETWEEN %s AND %s AND restrict <> %s ORDER BY random() LIMIT 1', ['High Carb', totalCal/3.2, totalCal/1.5, 'Breakfast'])
      for p in food5q:
         food5 = p
         cal5 = 1.5*float(food5.foodCal)
      total = cal1 + cal2 + cal3 + cal4 + cal5
      inserts = recipeTable(user = personId, totalCal = total, foodItem1 = food1.foodName, cal1 = cal1, foodItem2 = food2.foodName,
         cal2 = cal2, foodItem3 = food3.foodName, cal3 = food3.foodCal, foodItem4 = food4.foodName, cal4 = cal4,
         foodItem5 = food5.foodName, cal5 = cal5)
      inserts.save()
      return redirect('/recipe/')

def foodList(request):
   with connection.cursor() as cursor:
      cursor.execute('SELECT main_foodTable.foodName, main_foodTable.foodCal, count(main_foodTable.foodId) AS num FROM main_foodTable JOIN main_recipeTable ON(foodItem1 = foodName OR foodItem2 = foodName OR foodItem3 = foodName OR foodItem4 = foodName OR foodItem5 = foodName) GROUP BY foodId Order By num desc LIMIT 5')
      topFood = dictfetchall(cursor)
   with connection.cursor() as cursor:
      cursor.execute('SELECT user, count(*) AS num FROM main_recipeTable GROUP BY user ORDER BY num desc LIMIT 3')
      users = dictfetchall(cursor)
   return render(request, 'foodList.html',
   {'topFood' : topFood,
   'users' : users})

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
