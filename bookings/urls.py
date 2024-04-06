from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('table_bookings/', views.table_bookings, name='table_bookings'),
]