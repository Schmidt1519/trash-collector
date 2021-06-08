from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create_employee_profile, name="create_employee_profile"),
    path('daily_view/', views.daily_view, name="daily_view"),
    path('confirm/<int:customers_id>', views.confirm, name="confirm")

]