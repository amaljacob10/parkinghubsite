# Generated by Django 4.2.6 on 2024-02-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0020_eventbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventbooking',
            name='time',
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='intime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='outtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]