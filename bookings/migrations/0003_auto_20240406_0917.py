# Generated by Django 3.2.25 on 2024-04-06 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20240403_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='num_people',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=2, help_text='For reservations of bigger parties please contact us directly.'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[(datetime.time(17, 0), '5:00 PM'), (datetime.time(17, 30), '5:30 PM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(18, 30), '6:30 PM'), (datetime.time(19, 0), '7:00 PM'), (datetime.time(19, 30), '7:30 PM'), (datetime.time(20, 0), '8:00 PM'), (datetime.time(20, 30), '8:30 PM'), (datetime.time(21, 0), '9:00 PM')], default=datetime.time(17, 30)),
        ),
    ]
