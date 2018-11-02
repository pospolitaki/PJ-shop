from django.shortcuts import render
from product.models import *
from django.contrib.auth.decorators import login_required


# @login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'product/product_detail.html', locals())
