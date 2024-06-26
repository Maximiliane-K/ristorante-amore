from django.db import models
from django.contrib.auth.models import User
import datetime


class Booking(models.Model):
    """
    Model for table bookings
    """
    TIMES = []
    for hrs in range(17, 22):
        for min in range(0, 60, 30):
            if hrs < 21 or (hrs == 21 and min == 0):
                time_value = datetime.time(hrs, min)
                time_text = (
                    f"{hrs % 12 or 12}:{min:02d}"
                    f"{'AM' if hrs < 12 else 'PM'}"
                )
                TIMES.append((time_value, time_text))

    PAX_CHOICES = [(i, str(i)) for i in range(1, 11)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_last_name = models.CharField(max_length=400, default="", null=False)
    phone_number = models.CharField(max_length=20, null=False)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(choices=TIMES, default=datetime.time(17, 30))
    num_people = models.IntegerField(
        choices=PAX_CHOICES,
        null=False,
        default=2,
        help_text="For reservations of bigger parties please call us directly."
    )

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f'{self.user.username} - {self.date} {self.time}'
