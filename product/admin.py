from django.contrib import admin
from .models import *
# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    
    list_editable = (
        'category',
        'is_active',
        'discount',
        'for_children',
    )
    
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [ProductInline]

    list_editable = (
        'name',
        'name_ru',
        'name_en',
    )
    
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)