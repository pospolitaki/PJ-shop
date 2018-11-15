from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


from django.db import models

from accounts.models import Profile
from product.models import Product

class Status(models.Model):
    name = models.CharField(_('name'), max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(_('is active'), default=True)
    updated = models.DateTimeField(_('updated'), auto_now=True, auto_now_add=False)
    created = models.DateTimeField(_('created'), auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(_('is ordered'), default=False)
    date_added = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    date_ordered = models.DateTimeField(_('date ordered'), null=True)
    #added fields
    nmb = models.IntegerField(_('quantity'), default=1)
    details = models.CharField(_('details'), max_length=140, blank=True)
    price_per_item = models.DecimalField(_('price per item'), max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(_('total price'), max_digits=10, decimal_places=2, default=0) #price * nmb
    updated = models.DateTimeField(_('updated'), auto_now=True, auto_now_add=False)
    
    def save(self, *args, **kwargs):
        self.price_per_item = (self.product.price - self.product.price * self.product.discount / 100)
        self.total_price = self.nmb * self.price_per_item
        
        
        super(OrderItem, self).save(*args, **kwargs)
    #finish edding


    def __str__(self):
        return (self.product.name + " " + "(" + self.details + ")" + " × " + str(self.nmb))

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order items')


class Order(models.Model):
    ref_code = models.CharField(_('order code'), max_length=15)
    owner = models.ForeignKey(Profile, verbose_name=_('owner'), on_delete=models.SET_NULL, null=True, related_name='orders')
    is_ordered = models.BooleanField(_('is ordered'), default=False)
    items = models.ManyToManyField(OrderItem, verbose_name=_('items'))
    date_ordered = models.DateTimeField(_('date ordered'), auto_now=True)

    #added custom fields
    customer_email = models.EmailField(_('customer email'), blank=True, null=True, default=None)
    #phone number validation
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number should be entered in the format: '+38099.......'.")
    customer_phone_number = models.CharField(_('customer phone number'), validators=[phone_regex], max_length=17, blank=True) 

    status = models.ForeignKey(Status, verbose_name=_('status'), on_delete=models.SET_NULL, null=True, blank=True, default=1)


    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        # return sum([item.product.price for item in self.items.all()])
        return sum([item.total_price for item in self.items.all()])


    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
    
    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

        