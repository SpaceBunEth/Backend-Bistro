from django.urls import path

from . import views

urlpatterns = [
    path('menuitems/', views.get_items),
    path('items/', views.get_menu),
]