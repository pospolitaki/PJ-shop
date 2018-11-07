from django.contrib import admin

from .models import OrderItem, Order, Transaction, Status

# admin.site.register(OrderItem)
# admin.site.register(Order)
# admin.site.register(Transaction)



class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
 
    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
 
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
 
    class Meta:
        model = OrderItem

admin.site.register(OrderItem, OrderItemAdmin)


