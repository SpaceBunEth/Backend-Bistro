from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from pprint import pprint

from .models import Cuisine, Category, Dish_item
# Create your views here.

def get_items(request):
    pprint(dir(request))
    return HttpResponse('Hello World!!!')

def get_menu(request):
    
    items = Dish_item.objects.all()
    data = []
    for item in items:
        cuisine = Cuisine.objects.get(id=item.cuisine_id)
        category = Category.objects.get(id=item.category_id)
        
        item_dict = {
            'title': item.title,
            'description':item.description,
            'price':item.price,
            'spice_level':item.spice_level,
            'cuisine':{
                'id': cuisine.id,
                'title': cuisine.title,
            },
            'category':{
                'id':category.id,
                'title':category.title,
            },
        }

        data.append(item_dict)

    return JsonResponse(data, safe=False)