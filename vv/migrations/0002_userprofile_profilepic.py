# Generated by Django 4.2.3 on 2023-09-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]