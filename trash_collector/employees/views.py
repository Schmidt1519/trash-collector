from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'employees/index.html', context)


def confirm(request):
    customer = apps.get_model('customers.Customer')
    customer.balance
    return render(request, 'employees/index.html')
