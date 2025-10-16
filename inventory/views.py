from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import (
    ProductSerializer, 
    ProductDetailSerializer,
    CategorySerializer
)


class ProductListCreateView(generics.ListCreateAPIView):
    
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'price', 'quantity', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and 'detailed' in self.request.query_params:
            return ProductDetailSerializer
        return ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.select_related('category')
    serializer_class = ProductDetailSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    
    queryset = Category.objects.prefetch_related('products')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Category.objects.prefetch_related('products')
    serializer_class = CategorySerializer