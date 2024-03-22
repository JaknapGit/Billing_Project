from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Offers,GST, ProductCategory,Product
from .serializers import ProductCategorySerializer,ProductSerializer,OffersSerializer,GSTSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404



class OffersAPI(APIView):
    
    def get(self,request):
        try:
            offers=Offers.objects.all()
            serializer=OffersSerializer(offers, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={'detail':"There is an error fetching the offers"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request):
        try:
            serializer=OffersSerializer(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response (data=serializer.data, status=status.HTTP_201_CREATED)
            
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class OffersdetailAPI(APIView):
    
    def get(self, request, pk=None):
        try:
            offers=get_object_or_404(Offers, pk=pk)
            serializer=OffersSerializer(offers)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the offers"}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None):
        try:
            offers=get_object_or_404(Offers, pk=pk)
            serializer=OffersSerializer(data=request.data, instance=Offers)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, pk=None):
        try:
            offers=get_object_or_404(Offers, pk=pk)
            serializer=OffersSerializer(data=request.data, instance=offers, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
 
    
    def delete(self, request, pk=None):
        try:
            offers=get_object_or_404(Offers, pk=pk)
            offers.delete()
            return Response(data=None, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the products"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class GSTAPI(APIView):
    
    def get(self,request):
        try:
            gst=GST.objects.all()
            serializer=GSTSerializer(gst, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={'detail':"There is an error"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request):
        try:
            serializer=GSTSerializer(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response (data=serializer.data, status=status.HTTP_201_CREATED)
            
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class GSTdetailAPI(APIView):
    
    def get(self, request, pk=None):
        try:
            gst=get_object_or_404(GST, pk=pk)
            serializer=GSTSerializer(gst)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the gst details"}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None):
        try:
            gst=get_object_or_404(GST, pk=pk)
            serializer=GSTSerializer(data=request.data, instance=gst)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, pk=None):
        try:
            gst=get_object_or_404(GST, pk=pk)
            serializer=GSTSerializer(data=request.data, instance=gst, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
 
    
    def delete(self, request, pk=None):
        try:
            gst=get_object_or_404(GST, pk=pk)
            gst.delete()
            return Response(data=None, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the gst"}, status=status.HTTP_400_BAD_REQUEST)
        



class ProductCategoryAPI(APIView):
    
    def get(self,request):
        try:
            productcategory=ProductCategory.objects.all()
            serializer=ProductCategorySerializer(productcategory, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={'detail':"There is an error fetching ProductCategory"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request):
        try:
            serializer=ProductCategorySerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ProductCategorydetailAPI(APIView):
    
    def get(self, request, pk=None):
        try:
            productcategory=get_object_or_404(ProductCategory, pk=pk)
            serializer=ProductCategorySerializer(productcategory)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the Product Category"}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None):
        try:
            productcategory=get_object_or_404(ProductCategory, pk=pk)
            serializer=ProductCategorySerializer(data=request.data, instance=productcategory)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, pk=None):
        try:
            productcategory=get_object_or_404(ProductCategory, pk=pk)
            serializer=ProductCategorySerializer(data=request.data, instance=productcategory, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
 
    
    def delete(self, request, pk=None):
        try:
            productcategory=get_object_or_404(ProductCategory, pk=pk)
            productcategory.delete()
            return Response(data=None, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the gst"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class ProductAPI(APIView):
    
    def get(self,request):
        try:
            product=Product.objects.all()
            serializer=ProductSerializer(product, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={'detail':"There is an error fetching Product"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request):
        try:
            serializer=ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class ProductdetailAPI(APIView):
    
    def get(self, request, pk=None):
        try:
            product=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializer(product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the Product detail"}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None):
        try:
            product=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializer(data=request.data, instance=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, pk=None):
        try:
            product=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializer(data=request.data, instance=product, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
 
    
    def delete(self, request, pk=None):
        try:
            product=get_object_or_404(Product, pk=pk)
            product.delete()
            return Response(data=None, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data={'detail':"There is an error fetching the Product"}, status=status.HTTP_400_BAD_REQUEST)
        
        