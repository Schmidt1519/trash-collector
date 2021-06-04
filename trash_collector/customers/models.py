from django.db import models
# Create your models here.


<<<<<<< HEAD
#    user = models.ForeignKeyField(max_length=50)


# TODO: Finish customer model by adding necessary properties to fulfill user stories


=======
>>>>>>> 6a62b5364d9eb055334ce451968a1f57e38a762b
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    pickup_day = models.CharField(max_length=50)
    balance = models.IntegerField()
    one_time_pickup = models.DateField()
    suspension_start = models.DateField()
    suspension_end = models.DateField()
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
<<<<<<< HEAD
        return self
=======
        return self
>>>>>>> 6a62b5364d9eb055334ce451968a1f57e38a762b
