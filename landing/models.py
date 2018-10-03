from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128, verbose_name = _('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Shop Subscriber')
        verbose_name_plural = _('Shop Subscribers')
