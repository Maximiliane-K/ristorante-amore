# Generated by Django 3.2.25 on 2024-04-03 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date', 'time']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest_last_name',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(default='Please enter your contact number', max_length=35),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('17:30', '5:30 PM'), ('18:00', '6:00 PM'), ('18:30', '6:30 PM'), ('19:00', '7:00 PM'), ('19:30', '7:30 PM'), ('20:00', '8:00 PM'), ('20:30', '8:30 PM')], default='17:30'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_people',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='For reservations of bigger parties please contact us directly.'),
        ),
    ]