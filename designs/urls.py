from django.urls import path
from . import views

app_name = 'designs'

urlpatterns = [
    path('<slug:proj_id>/', views.project, name='project'),
    path('', views.designs, name='designs'),
]