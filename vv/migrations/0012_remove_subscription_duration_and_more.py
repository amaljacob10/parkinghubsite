# Generated by Django 4.2.6 on 2024-01-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0011_subscription_userprofile_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='name',
        ),
        migrations.AddField(
            model_name='subscription',
            name='features',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='subscription',
            name='sub_type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='validity',
            field=models.CharField(blank=True, choices=[('1 MONTH', '1 MONTH'), ('2 MONTH', '2 MONTH'), ('3 MONTH', '3 MONTH'), ('4 MONTH', '4 MONTH'), ('5 MONTH', '5 MONTH'), ('6 MONTH', '6 MONTH'), ('7 MONTH', '7 MONTH'), ('8 MONTH', '8 MONTH'), ('9 MONTH', '9 MONTH'), ('10 MONTH', '10 MONTH'), ('11 MONTH', '11 MONTH'), ('12 MONTH', '12 MONTH')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]