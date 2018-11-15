from django.contrib import admin

from .models import OrderItem, Order, Status
from django.utils.translation import gettext_lazy as _

# admin.site.register(OrderItem)
# admin.site.register(Order)
# admin.site.register(Transaction)



class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
 
    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderItemInline(admin.TabularInline):
    model = Order.items.through  
    extra = 0

    fields = ['product', 'nmb', 'details','price_per_item', 'total_price']
    readonly_fields = ['product', 'nmb', 'details', 'price_per_item', 'total_price']

    def product(self, instance):
        return instance.orderitem.product
    product.short_description = _('product')

    def nmb(self, instance):
        return instance.orderitem.nmb
    nmb.short_description = _('quantity')

    def details(self, instance):
        return instance.orderitem.details
    details.short_description = _('details')

    def price_per_item(self, instance):
        return instance.orderitem.price_per_item
    price_per_item.short_description = _('price per item')

    def total_price(self, instance):
        return instance.orderitem.total_price
    total_price.short_description = _('total price')

    verbose_name = _("order item")
    verbose_name_plural = _("order items")

class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    list_display = [field.name for field in Order._meta.fields]
    readonly_fields = ('date_ordered',)
    list_filter = ['status']
    search_fields = ('ref_code', 'owner__user__username', 'customer_email', 'status__name', 'customer_phone_number')
    

    list_editable = (
        'status',
    )

    exclude = ['items']

    inlines = [
        OrderItemInline,
    ]
    
        

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
 
    class Meta:
        model = OrderItem

admin.site.register(OrderItem, OrderItemAdmin)


