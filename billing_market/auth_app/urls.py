from django.urls import path
from .views import UserView, SingleUserView

urlpatterns = [
    path('user/', UserView.as_view(), name='user'),
    path('user/<int:pk>/', SingleUserView.as_view(), name='single')
]