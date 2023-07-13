from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', CityList.as_view()),
]
