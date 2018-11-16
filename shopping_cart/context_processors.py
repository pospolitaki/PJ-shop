def cart_items_amount(request):
    if request.user.is_authenticated():
        pending_order = request.user.profile.orders.filter(is_ordered=False).first()
        if pending_order:
            cart_items_amount = sum([item.nmb for item in pending_order.items.all()])
        else: 
            cart_items_amount = 0
    return locals()
    

from django.conf import settings # import the settings file

def get_settings(request):
    return {'settings': settings}