from django.shortcuts import render
from product.models import *


def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()

    return render(request, 'product/product_detail.html', locals())
