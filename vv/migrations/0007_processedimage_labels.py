# Generated by Django 4.2.3 on 2023-10-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0006_processedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='processedimage',
            name='labels',
            field=models.TextField(default=''),
        ),
    ]
