from django.contrib.auth.models import User, Group
from .models import Dish_item, Category, Cuisine
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
        
class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['title']

# router.register change to ModelSerializer
class DishSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer() #must have _id at the end foreign key
    cuisine = CuisineSerializer()
    class Meta:
        model = Dish_item
        fields = ['title', 'description', 'price','spice_level','category', 'cuisine']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']