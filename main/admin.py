from django.contrib import admin
from .models import post_data, foodTable, recipeTable
# Register your models here.
admin.site.register(post_data)
admin.site.register(foodTable)
admin.site.register(recipeTable)