from django.db import models

# Create your models here.


class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    user = models.ForeignKeyField(max_length=50)

    def __str__(self):
        return self
# TODO: Create an Employee model with properties required by the user stories