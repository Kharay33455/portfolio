from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.base, name='base'),
    path('message/', views.message, name='message'),
    path('book-a-service/', views.booking, name='booking'),
]