from rest_framework import serializers
from .models import Offers, GST, ProductCategory,Product


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offers
        fields='__all__'
        
        

class GSTSerializer(serializers.ModelSerializer):
    class Meta:
        model=GST
        fields='__all__'
        
        


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'
        
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'