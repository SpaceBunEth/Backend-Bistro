from django.db import models

# Create your models here.

class cuisine(models.Model):
    title = models.CharField(max_length=30)

class category(models.Model):
    title = models.CharField(max_length=30)

class item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    spice_level = models.IntegerField()
    cuisine = models.ForeignKey(cuisine, on_delete=models.PROTECT)
    category = models.ForeignKey(category, on_delete=models.PROTECT)

    