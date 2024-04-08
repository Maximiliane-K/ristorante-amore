from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.about_view, name='home'),
    path('food/', views.foodmenu, name='food'),
    path('drinks/', views.beveragemenu, name='drinks'),
    path('contact/', views.contact, name='contact'),
]
