from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'bookings'

urlpatterns = [
    path('table_bookings/', views.table_bookings, name='table_bookings'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('booking_successful/', views.booking_successful, name='booking_successful'),
]