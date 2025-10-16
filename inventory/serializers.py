from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):

    products_count = serializers.IntegerField(source='products.count', read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
   
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'category_name', 
                  'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'category_name']

class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True
    )
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'category_id',
                  'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']











