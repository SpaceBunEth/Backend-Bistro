from django.contrib import admin

from .models import Cuisine, Category, Dish_item

admin.site.register(Cuisine)
admin.site.register(Category)
admin.site.register(Dish_item)

# Register your models here.
