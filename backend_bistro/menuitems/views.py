# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from pprint import pprint
# from .models import Cuisine, Category, Dish_item

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Dish_item, Category, Cuisine
from menuitems.serializers import UserSerializer, GroupSerializer, DishSerializer, CategorySerializer, CuisineSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CuisineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cuisine to be viewed or edited.
    """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Dish to be viewed or edited.
    """
    queryset = Dish_item.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ----------------
# def get_items(request):
#     pprint(dir(request))
#     return HttpResponse('Hello World!!!')

# def get_menu(request):
    
#     items = Dish_item.objects.all()
#     data = []
#     for item in items:
#         cuisine = Cuisine.objects.get(id=item.cuisine_id)
#         category = Category.objects.get(id=item.category_id)
        
#         item_dict = {
#             'title': item.title,
#             'description':item.description,
#             'price':item.price,
#             'spice_level':item.spice_level,
#             'cuisine':{
#                 'id': cuisine.id,
#                 'title': cuisine.title,
#             },
#             'category':{
#                 'id':category.id,
#                 'title':category.title,
#             },
#         }

#         data.append(item_dict)

#     return JsonResponse(data, safe=False)