from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Booking(models.Model):
    """
    Model for table bookings
    """

    # Restaurant opening hours the guest can choose from
    HOURS_CHOICES = [
        ('17:30', '5:30 PM'),
        ('18:00', '6:00 PM'),
        ('18:30', '6:30 PM'),
        ('19:00', '7:00 PM'),
        ('19:30', '7:30 PM'),
        ('20:00', '8:00 PM'),
        ('20:30', '8:30 PM'),
    ]

    # Choice for number of guests 
    PAX_CHOICES = [(i, str(i)) for i in range(1, 11)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_last_name = models.CharField(max_length=400, default="", null=False)
    phone_number = models.CharField(max_length=35, default="Please enter your contact number", null=False)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(choices=HOURS_CHOICES, default="17:30")
    num_people = models.IntegerField(choices=PAX_CHOICES, null=False, help_text="For reservations of bigger parties please contact us directly.")

    class Meta:
        ordering = ['date', 'time']

    def clean_fields(self):
        if self.date < datetime.date.today():
            raise ValidationError("Please select a date in the future fpr your booking.")

    def __str__(self):
        return f'{self.user.username} - {self.date} {self.time}'
