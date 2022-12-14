# Generated by Django 4.1.1 on 2022-09-18 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showtime', '0002_shows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_date', models.DateField(auto_now_add=True)),
                ('seats', models.IntegerField()),
                ('is_valid', models.BooleanField(default=True)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='showtime.shows')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
