from django.urls import path
from .views import VendorView, OrdersApi

urlpatterns = [
    path('orders/', OrdersApi.as_view(), name='orders'),
]
