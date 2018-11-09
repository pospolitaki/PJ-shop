from __future__ import unicode_literals
from django.core.validators import RegexValidator

from django.db import models

from accounts.models import Profile
from product.models import Product

class Status(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_ordered = models.DateTimeField(null=True)
    #added fields
    nmb = models.IntegerField(default=1)
    details = models.CharField(max_length=140, blank=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price * nmb
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def save(self, *args, **kwargs):
        self.price_per_item = (self.product.price - self.product.price * self.product.discount / 100)
        self.total_price = self.nmb * self.price_per_item
        
        
        super(OrderItem, self).save(*args, **kwargs)
    #finish edding


    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='orders')
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    #added custom fields
    customer_email = models.EmailField(blank=True, null=True, default=None)
    #phone number validation
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number should be entered in the format: '+38099.......'.")
    customer_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # customer_phone = models.CharField(max_length=128, blank=True, null=True, default=None)

    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, default=1)


    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        # return sum([item.product.price for item in self.items.all()])
        return sum([item.total_price for item in self.items.all()])


    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


        