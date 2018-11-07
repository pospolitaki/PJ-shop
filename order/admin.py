from django.contrib import admin
from .models import *
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1

# class StatusAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Status._meta.fields]
 
#     class Meta:
#         model = Status

# admin.site.register(Status, StatusAdmin)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Order1._meta.fields]
#     inlines = [ProductInOrderInline]

#     class Meta:
#         model = Order1

# admin.site.register(Order1, OrderAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)