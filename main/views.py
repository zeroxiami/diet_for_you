from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import post_data
from django.db import connection, transaction

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