from django.urls import path, include
from rest_framework import routers
from api import views

from . import views

urlpatterns = [
    path('locations/<str:city>/', views.WeatherDetail.as_view()),
]