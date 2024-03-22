from django.urls import path
from .views import ProductCategoryAPI, ProductAPI,OffersAPI,GSTAPI
from .views import OffersdetailAPI, GSTdetailAPI, ProductCategorydetailAPI, ProductdetailAPI

urlpatterns=[
    
    path('offers/', OffersAPI.as_view()),
    path('offers/<int:pk>/', OffersdetailAPI.as_view()),
    path('productcategory/', ProductCategoryAPI.as_view()),
    path('productcategory/<int:pk>/', ProductCategorydetailAPI.as_view()),
    path('product/', ProductAPI.as_view()),
    path('product/<int:pk>/', ProductdetailAPI.as_view()),
    path('gst/', GSTAPI.as_view()),
    path('gst/<int:pk>/', GSTdetailAPI.as_view()),
    
    
]