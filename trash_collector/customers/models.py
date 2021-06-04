from django.db import models
# Create your models here.


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance = models.IntegerField()
    one_time_pickup = models.DateField()
    suspension_start = models.DateField()
    suspension_end = models.DateField()
    user = models.ForeignKeyField(max_length=50)

    def __str__(self):
        return self
# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
