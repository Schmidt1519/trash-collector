from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
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


def create_employee_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        user = request.user
        new_employee = Employees(name=name, address=address, zip_code=zip_code, user=user)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/employee_profile.html')


def daily_view(request):
    user = request.user
    employee = Employees.objects.filter(user=user)

    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    context = {"customer": customer}

# add further filters here
    if customer.zip_code == employee.zip_code:
        return render(request, 'employees/daily_view.html', context)

def confirm(request):
    customer = apps.get_model('customers.Customer')
    customer.balance
    return render(request, 'employees/index.html')
