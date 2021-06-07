from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create_profile, name='create_profile'),
    path('detail/', views.detail, name='detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('one-time-pickup/', views.one_time_pickup, name='one_time_pickup'),
    path('suspend-service/', views.suspend_service, name='suspend'),
]
