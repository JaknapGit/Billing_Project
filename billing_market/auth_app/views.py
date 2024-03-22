from django.shortcuts import render
from rest_framework.response import Response
from .serializers import User, UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .permissions import IsOwnerOrManager, IsOwnerOrManagerOrCreateOnly
from rest_framework import status
from rest_framework.authentication import TokenAuthentication



class UserView(APIView):
   # authentication_classes = [TokenAuthentication]
   # permission_classes = [IsOwnerOrManagerOrCreateOnly]

    def get(self, request):
        try:
            data = User.objects.all()
            serialize = UserSerializer(data, many=True)           
            return Response(data=serialize.data, status=200)
        except Exception as msg:
            return Response(data=serialize.errors, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=201)
        return Response(data=serialize.errors, status=404)
    
class SingleUserView(generics.GenericAPIView):
    permission_classes = [IsOwnerOrManager]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        try:
            data = self.get_object()
            serialize = UserSerializer(data)
            #print(args)
            #print(kwargs)
            #print(request)
            return Response(data=serialize.data, status=200)
        except User.DoesNotExist as msg:
            return Response(data={'details':'User Not Found'})
        
    def patch(self, request, *arg, **kwarg):
        try:
            print('executed try')
            obj = self.get_object()
            serialize = self.get_serializer(data=request.data, instance=obj, partial=True)
            if serialize.is_valid():
                obj = serialize.save()
                return Response(data=serialize.data, status=status.HTTP_202_ACCEPTED)
        except Exception as msg:
            print('executed except')
            return Response(data={'bad request'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *arg, **kwarg):
        try:
            obj = self.get_object()
        except Exception as msg:
            pass



