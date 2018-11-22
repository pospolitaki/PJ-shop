from django.shortcuts import render
from product.models import *
from shopping_cart.models import Order
from django.contrib.auth.decorators import login_required


# @login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    current_order_products = []
    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

    context = {
    'product': product,
    }
    if current_order_products:
        context.update({'current_order_products': current_order_products})
    return render(request, 'product/product_detail.html', context)
