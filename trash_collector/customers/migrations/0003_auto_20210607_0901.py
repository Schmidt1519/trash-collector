# Generated by Django 3.1.8 on 2021-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210604_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(blank=True, null=True),
        ),
    ]
