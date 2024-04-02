from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('table_booking', views.table_booking, name='table_booking'),
]