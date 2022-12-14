# Generated by Django 4.1.1 on 2022-09-20 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showtime', '0002_shows'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateField(auto_now_add=True)),
                ('seats', models.IntegerField()),
                ('is_paid', models.BooleanField(default=True)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows_booked', to='showtime.shows')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
