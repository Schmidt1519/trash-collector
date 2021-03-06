# Generated by Django 3.1.8 on 2021-06-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='pickup_day',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_end',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_start',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
