# Generated by Django 4.2.3 on 2023-09-13 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vv.park'),
        ),
    ]
