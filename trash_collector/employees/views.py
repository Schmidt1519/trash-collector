from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from datetime import datetime as dt
from datetime import datetime
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    logged_in_employee = Employees.objects.get(user=user)

    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()

    now = dt.now()
    today = now.strftime('%A')
    today_date = datetime.today().strftime('%Y-%m-%d')

    for item in customer:
        if not item.suspension_start:
            pass
        elif item.suspension_start.strftime('%Y-%m-%d') <= today_date <= item.suspension_end.strftime('%Y-%m-%d'):
            item.is_suspended = True
            item.save()
        else:
            item.is_suspended = False
            item.save()

    zip_customer = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    day_customer = zip_customer.filter(pickup_day=today) | zip_customer.filter(one_time_pickup=today_date)
    non_suspended_customer = day_customer.filter(is_suspended=False)

    # for item in customer:
    # if day_customer.suspension_start < today_date < day_customer.suspension_end:

    context = {
        "customer": customer,
        "employee": logged_in_employee,
        "zip_customer": zip_customer,
        "day_customer": day_customer,
        "non_suspended_customer": non_suspended_customer,
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
    logged_in_employee = Employees.objects.get(user=user)

    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    now = dt.now()
    today = now.strftime('%A')
    today_date = datetime.today().strftime('%Y-%m-%d')

    zip_customer = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    day_customer = zip_customer.filter(pickup_day=today) | zip_customer.filter(one_time_pickup=today_date)

    context = {
        "customer": customer,
        "employee": logged_in_employee,
        "zip_customer": zip_customer,
        "day_customer": day_customer,
    }
    return render(request, 'employees/daily_view.html', context)


def daily_view_update(request, day):
    user = request.user
    logged_in_employee = Employees.objects.get(user=user)

    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    now = dt.now()
    today = now.strftime('%A')
    today_date = datetime.today().strftime('%Y-%m-%d')

    zip_customer = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    day_customer = zip_customer.filter(pickup_day=day)


    context = {
        "customer": customer,
        "employee": logged_in_employee,
        "zip_customer": zip_customer,
        "day_customer": day_customer,
    }
    return render(request, 'employees/daily_view_update.html', context)


def confirm(request, customers_id):
    # use customer_id to get the Customer object from the db of the customer who is being confirmed
    # edit the balance property on that customer object to have charge added
    # save customer object after change
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customers_id)
    customer.balance = customer.balance + 5
    customer.save()
    return HttpResponseRedirect(reverse('employees:index'))


# def charge(request, customers_id):
#     Customer = apps.get_model('customers.Customer')
#     customer = Customer.objects.get(id=customers_id)
#     context = {'customer': customer}
#
#     if request.method == 'POST':
#         customer.balance = customer.balance + 5
#         customer.save()
#         return HttpResponseRedirect(reverse('employees:index'))
#     else:
#         return render(request, 'employees/charge.html', context)


# def customer_profile(request, customers_id):
#     Customer = apps.get_model('customers.Customer')
#     customer = Customer.objects.get(id=customers_id)
#     context = {"customer": customer}
#     return render(request,'employees:customer_profile', context)

