from rest_framework.viewsets import ModelViewSet
from .serializers import GST, GSTSerializer, ProductCategory, ProductCategorySerializer, Product, ProductSerializer, Offers, OffersSerializer
from rest_framework import status
from rest_framework.response import Response


class OffersApi(ModelViewSet):
    serializer_class = OffersSerializer
    queryset = Offers.objects.all()


class GSTApi(ModelViewSet):
    serializer_class = GSTSerializer
    queryset = GST.objects.all()


class ProductCategoryApi(ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProductApi(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
