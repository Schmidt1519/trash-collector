from django.db import models
from datetime import datetime
# Create your models here.


# TODO: Finish customer model by adding necessary properties to fulfill user stories



class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    pickup_day = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    one_time_pickup = models.DateField(blank=True, null=True)
    suspension_start = models.DateField(blank=True, null=True)
    suspension_end = models.DateField(blank=True, null=True)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self

