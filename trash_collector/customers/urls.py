from django.urls import path
from . import views

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create_profile, name='create_profile'),
    path('detail/', views.detail, name='detail'),
]