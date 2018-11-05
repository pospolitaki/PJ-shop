def cart_items_amount(request):
    if request.user.is_authenticated():
        cart_items_amount = request.user.profile.orders.filter(is_ordered=False).first()
        if cart_items_amount:
            cart_items_amount = cart_items_amount.items.count()
        else: 
            cart_items_amount = 0
    return locals()
    