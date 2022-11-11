from django.db import models

# Create your models here.

class Cuisine(models.Model):
    title = models.CharField(max_length=30)

class Category(models.Model):
    title = models.CharField(max_length=30)

class Dish_item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    spice_level = models.IntegerField()
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

