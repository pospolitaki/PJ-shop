from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from product.models import Product
# from shopping_cart.models import Order



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    purchases = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username

    def get_pending_order(self):
        return self.orders.filter(is_ordered=False)[0]
def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
