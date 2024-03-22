from .models import Vendor, Orders, OrderProducts
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')

class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        #fields = ('__all__')
        exclude = ('order',)

class OrderSerializer(serializers.ModelSerializer):
    orderProducts = OrderProductsSerializer(many=True, write_only=True)
    class Meta:
        model = Orders
        fields = ('__all__')

    def create(self, validated_data):
        orderproducts = validated_data.pop('orderProducts')
        order = Orders.objects.create(**validated_data)
        for product in orderproducts:
            OrderProducts.objects.create(order=order, **product)
        return super().create(validated_data)