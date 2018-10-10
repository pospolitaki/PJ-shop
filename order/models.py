from django.db import models
from product.models import Product
from django.db.models.signals import post_save


# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return 'Статус:{}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
    

class Order(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128)
    customer_phone = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_adress =models.CharField(max_length=128, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # total price for all products
    comment = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return 'Заказ {} : {}'.format(self.id, self.status)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def save(self, *args, **kwargs):
    #     super(Order, self).save(*args, **kwargs)
        

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True,null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price * nmb
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
    
    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.nmb * self.price_per_item
        
        
        super(ProductInOrder, self).save(*args, **kwargs)
    
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
        
    order_total_price = 0

    for item in all_product_in_order:
        order_total_price += item.total_price
    
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        super(ProductInCart, self).save(*args, **kwargs)