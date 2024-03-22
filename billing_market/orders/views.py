from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import VendorSerializer, Vendor, Orders, OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class VendorView(ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    

class OrdersApi(APIView):
    # serializer_class = OrderSerializer
    # queryset = Orders.objects.all(), vendorData,

    def get(self, request):
        try:
            orderData = Orders.objects.all()
            orderSerializer = OrderSerializer(orderData, many=True)
            vendorData = Vendor.objects.all()
            serializer = VendorSerializer(vendorData, many=True)
            print('serialized')
            return Response(data=[serializer.data, orderSerializer.data], status=status.HTTP_200_OK)
        except:
            return Response(data={'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)