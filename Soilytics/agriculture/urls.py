from django.urls import path

from . import views

urlpatterns = [
    path('/', views.landing, name='home'),
    path('/soildata', views.soildata, name="soil-data"),
    path('/plantasium', views.plantdata, name="plant-data"),
]