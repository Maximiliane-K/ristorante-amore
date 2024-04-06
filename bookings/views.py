from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here
@login_required
def table_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            return redirect()
    else:
        form = BookingForm()

    return render(request, 'bookings/table_booking.html', {'form': form})