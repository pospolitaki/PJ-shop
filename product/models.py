from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', related_query_name="product",blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return _('{}'.format(self.name))

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, related_name='product_imgs')
    image = models.ImageField(upload_to='product_images')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'




