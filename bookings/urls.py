from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'bookings'

urlpatterns = [
    path('table_bookings/', views.table_bookings, name='table_bookings'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('booking_successful/', views.booking_successful, name='booking_successful'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout.html', views.logout_page, name='logout_page'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('booking/update/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('confirm-delete/<int:booking_id>/', views.confirm_delete, name='confirm_delete'),
]