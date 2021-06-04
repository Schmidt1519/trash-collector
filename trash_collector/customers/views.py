from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
=======
>>>>>>> 6a62b5364d9eb055334ce451968a1f57e38a762b
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')

<<<<<<< HEAD
=======

>>>>>>> 6a62b5364d9eb055334ce451968a1f57e38a762b
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        pickup_day = request.POST.get('pickup_day')
<<<<<<< HEAD
        new_customer = Customer(name=name, address=address, zip_code=zip_code, balance=balance, one_time_pickup=one_time_pickup, suspension_start=suspension_start, suspension_end=suspension_end, user=user)
=======
        # balance = request.POST.get('balance')
        # one_time_pickup = request.POST.get('one_time_pickup')
        # suspension_start = request.POST.get('suspension_start')
        # suspension_end = request.POST.get('suspension_end')
        new_customer = Customer(name=name, address=address, zip_code=zip_code, pickup_day=pickup_day)
        # new_customer = Customer(name=name, address=address, zip_code=zip_code, balance=balance, one_time_pickup=one_time_pickup, suspension_start=suspension_start, suspension_end=suspension_end)
>>>>>>> 6a62b5364d9eb055334ce451968a1f57e38a762b
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')