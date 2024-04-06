from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


def booking_successful(request):
    """
    View for displaying the successful booking page
    """
    latest_booking = Booking.objects.latest('id')  

    context = {'latest_booking': latest_booking}
    
    return render(request, 'bookings/booking_successful.html', context)
