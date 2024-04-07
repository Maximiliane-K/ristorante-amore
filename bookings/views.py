from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied


# Create your views here
@login_required
def table_bookings(request):
    """
    View for displaying booking form
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            return redirect('bookings:booking_successful')
    else:
        form = BookingForm()
    
    context = {'form': form}

    return render(request, 'bookings/table_booking.html', context)


def register(request):
    """
    View for displaying the register form for users to create an account
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bookings:table_bookings')
    else:
        form = UserCreationForm()
    
    context = {'form': form}

    return render(request, 'registration/register.html', context)


def booking_successful(request):
    """
    View for displaying the successful booking page
    """
    latest_booking = Booking.objects.latest('id')  

    context = {'latest_booking': latest_booking}
    
    return render(request, 'bookings/booking_successful.html', context)


def logout_page(request):
    return render(request, 'registration/logout.html')


def view_bookings(request):
    """
    View for displaying the list of bookings
    """
    user_bookings = Booking.objects.filter(user=request.user)
    
    context = {'user_bookings': user_bookings}

    return render(request, 'bookings/view_bookings.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    View for displaying booking form to be able to edit exsisting booking
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user != booking.user:  
        raise PermissionDenied

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.instance.status = 0  
            form.save()
            return redirect()  
    else:
        form = BookingForm(instance=booking)

    context = {'form': form}

    return render(request, 'bookings/table_booking.html', context)
