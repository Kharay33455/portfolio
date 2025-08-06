from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.base, name='base'),
    path('message/', views.message, name='message'),
    path('book-a-service/', views.booking, name='booking'),
    path('web3', views.web3, name = 'web3'),
    path("get-data", views.fetch_data, name="fetch_data")
]