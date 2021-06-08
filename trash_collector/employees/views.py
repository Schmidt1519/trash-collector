from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from datetime import date
import calendar
from datetime import datetime as dt
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    logged_in_employee = Employees.objects.get(user=user)

    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()

    # datetime_object = datetime.datetime.now()
    # day = date.today()
    # calendar.day_time[day.weekday()]
    now = dt.now()
    today = now.strftime('%A')

    zip_customer = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    day_customer = zip_customer.filter(pickup_day=today)

    context = {
        "customer": customer,
        "employee": logged_in_employee,
        "zip_customer": zip_customer,
        "day_customer": day_customer,
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


    # show all customers and ability to filter by day
def daily_view(request):
    pass


# def confirm(request, customer_id):
#     customer = apps.get_model('customers.Customer')
#     customer.balance
#     return HttpResponseRedirect(reverse('employees:index'))
