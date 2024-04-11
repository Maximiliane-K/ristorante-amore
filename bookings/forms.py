from django import forms
from .models import Booking
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'guest_last_name',
            'phone_number',
            'date',
            'time',
            'num_people'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
