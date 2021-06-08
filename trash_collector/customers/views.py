from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    try:
        logged_in_customer = Customer.objects.get(user=user)
        context = {'logged_in_customer': logged_in_customer}
    except:
        return HttpResponseRedirect(reverse('customers:create_profile'))

    print(user)
    return render(request, 'customers/index.html', context)


def detail(request):
    user = request.user
    customer_detail = Customer.objects.get(user=user)
    context = {"customer_detail": customer_detail}
    return render(request, 'customers/detail.html', context)


def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        pickup_day = request.POST.get('pickup_day')
        user = request.user
        new_customer = Customer(name=name, address=address, zip_code=zip_code, pickup_day=pickup_day, user=user)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:detail'))
    else:
        return render(request, 'customers/create.html')


def edit_profile(request):
    user = request.user
    customer_edit_profile = Customer.objects.get(user=user)
    context = {"customer_edit_profile": customer_edit_profile}

    if request.method == 'POST':
        edit_profile = Customer.objects.get(user=user)
        edit_profile.name = request.POST.get('name')
        edit_profile.address = request.POST.get('address')
        edit_profile.zip_code = request.POST.get('zip_code')
        edit_profile.pickup_day = request.POST.get('pickup_day')
        edit_profile.save()
        return HttpResponseRedirect(reverse('customers:detail'))
    else:
        return render(request, 'customers/edit_profile.html', context)


def one_time_pickup(request):
    user = request.user
    customer_one_time_pickup = Customer.objects.get(user=user)
    context = {"customer_one_time_pickup": customer_one_time_pickup}

    if request.method == 'POST':
        edit_one_time_pickup = Customer.objects.get(user=user)
        edit_one_time_pickup.one_time_pickup = request.POST.get('one_time_pickup')
        edit_one_time_pickup.save()
        return HttpResponseRedirect(reverse('customers:detail'))
    else:
        return render(request, 'customers/one_time_pickup.html', context)


def suspend_service(request):
    user = request.user
    customer_suspend_service = Customer.objects.get(user=user)
    context = {"customer_suspend_service": customer_suspend_service}

    if request.method == 'POST':
        edit_suspend_service = Customer.objects.get(user=user)
        edit_suspend_service.suspension_start = request.POST.get('suspension_start')
        edit_suspend_service.suspension_end = request.POST.get('suspension_end')
        edit_suspend_service.save()
        return HttpResponseRedirect(reverse('customers:detail'))
    else:
        return render(request, 'customers/suspend.html', context)
