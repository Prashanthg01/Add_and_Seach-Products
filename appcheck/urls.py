from django.urls import path
from . import views

app_name = 'appagri'

urlpatterns = [
    path('', views.home, name='home'),
]