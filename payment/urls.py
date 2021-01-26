from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('success' , views.success , name='pay-success')
]
