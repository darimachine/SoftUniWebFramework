
from django.shortcuts import render
from rest_framework import generics as api_views, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from api.models import Product, Category

from rest_framework import permissions
# This should in file serializers.py
class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
class ProductSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializerOnly(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id', 'name','price']
class FullCategorySerializer(serializers.ModelSerializer):

    product_set = ProductSerializerOnly(many=True)
    class Meta:
        model = Category
        fields = '__all__'

# Create your views here.
class ManualProductListView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        seriliazer = ProductSerializer(queryset, many=True)
        return Response(seriliazer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def list(self, request, *args, **kwargs):
        print(self.request.user)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ProductsCreateView(api_views.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer

class SinglePdocutView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer