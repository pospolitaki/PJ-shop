from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal, getcontext

getcontext().prec = 2

# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name') ,max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')



class Product(models.Model):
    name = models.CharField(_('name'), max_length=128, blank=True, null=True, default=':)')
    is_active = models.BooleanField(_('is active'), default=True)
    for_children = models.BooleanField(_('for children'), default=False)
    discount = models.IntegerField(_('discount'), default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', verbose_name=_('category'), related_query_name="product",blank=True, null=True, default=None)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0)
    description = models.TextField(_('description'), blank=True, null=True, default=_('Nice to meet you :)'))
    created = models.DateTimeField(_('created'), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
    
    @property
    def new_price(self):
        return float(self.price - self.price * Decimal(self.discount / 100))
        
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name=_('product'),related_name='product_imgs')
    image = models.ImageField(_('image'), upload_to='product_images')
    is_main = models.BooleanField(_('is main'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    created = models.DateTimeField(_('created'), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')




