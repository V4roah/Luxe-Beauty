from django.db import models


   
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
        
    def __str__(self):
        return self.name

   

class Product(models.Model):
    price_type_choices = (
        ('unitario', 'Precio Unitario'),
        ('media-doc', 'Media Docena'),
        ('docena', 'Docena'),
        ('por-kilo', 'Por Kilo'),
        
    )
    
    name = models.CharField(max_length=255, verbose_name='Nombre')
    image = models.ImageField(upload_to='products', verbose_name='Imagen', default="imagen_default.png")
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='get_products',verbose_name='Categoría')
    price_type = models.CharField(max_length=20, choices=price_type_choices, verbose_name='Tipo de Precio', default="unitario")
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
  
    