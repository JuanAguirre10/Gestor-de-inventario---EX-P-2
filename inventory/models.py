from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name='Nombre')
    quantity = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name='Cantidad'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Precio'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Categoría'
    )
    description = models.TextField(blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"