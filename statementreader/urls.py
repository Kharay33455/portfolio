
from django.urls import path
from .views import *

app_name="statementreader"

urlpatterns=[
    path('highlight/', highlight, name="highlight")
]
