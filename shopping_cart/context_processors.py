def cart_items_amount(request):
    if request.user.is_authenticated():
        cart_items_amount = request.user.profile.orders.filter(is_ordered=False)[0].items.count() or 0
    return locals()