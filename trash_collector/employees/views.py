from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from datetime import datetime as dt
from datetime import datetime
from django.contrib import messages
import requests
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    try:
        logged_in_employee = Employees.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create_employee_profile'))

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

    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()

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
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customers_id)
    customer.balance = customer.balance + 5
    customer.save()
    messages.success(request, 'Pickup Confirmed')
    return HttpResponseRedirect(reverse('employees:index'))


def customer_profile(request, customers_id):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customers_id)
    API_KEY = 'AIzaSyAAFgBqp3QjLkKkjrvqX_TniOmS6I0K73I'
    address = customer.address
    params = {
        'key': API_KEY,
        'address': address
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    response.keys()
    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
    context = {
        "customer": customer,
        "lon": lon,
        "lat": lat
               }
    return render(request, 'employees/customer_profile.html', context)