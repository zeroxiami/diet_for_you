"""diet_for_you URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import  personalInfo, edit, post_info, recipe, recipeDelete, recipeAdd, signup, profile, recipeUpdate, pastRecipe, foodList
from django.contrib.auth import views
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'Info', views.post_data_view, 'Info')
router.register(r'Recipes', views.recipeTable_view, 'Recipes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('main/', personalInfo),
    path('edit/', edit),
    path('edit/updateInfo/', post_info),
    path('recipe/', recipe),
    path('recipe/past/', pastRecipe),
    path('recipe/update/<int:foodItem>/<int:recipeId>', recipeUpdate),
    path('recipe/addNew/', recipeAdd),
    path('recipe/delete/<int:recipeId>/', recipeDelete),
    path('signup/', signup),
    path('profile/', profile),
    path('countList/', foodList),
    path('api/', include(router.urls))
]