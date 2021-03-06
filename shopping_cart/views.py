from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch
from django.template.loader import render_to_string

from accounts.models import Profile
from product.models import Product

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order

from shopping_cart.forms import OrderContactPhoneForm

from django.http import JsonResponse
from django.db import IntegrityError, transaction
from django.core.mail import send_mail, send_mass_mail, BadHeaderError,EmailMultiAlternatives

import datetime
import json


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    # order = Order.objects.prefetch_related('items__product__product_imgs').filter(owner=user_profile, is_ordered=False)
    order = Order.objects.prefetch_related(Prefetch('items', queryset=OrderItem.objects.select_related('product'))).filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

def generate_success_order_email_content(items_queryset):
    content = ''
    for item in items_queryset:
        content += f'{item.product.name} ({item.details}) × {item.nmb}\n'
    return content



# ajax + login_requiered cooperating
def add_to_cart(request, **kwargs):
    return_data = dict()

    if request.user.is_authenticated():
    # get the user profile
        user_profile = get_object_or_404(Profile, user=request.user)
        # filter products by id

        product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

        product_quantity = int(request.POST.get('quantity',1)) 
        order_item_details_raw = request.POST.get('order_item_details', '')

        #spliting data from ajax request, checkout here
        # if order_item_details_raw:
        #     try:
        #         order_item_details = order_item_details_raw.split(',')
        #         order_item_details = ', '.join([item.split(':')[1].strip() for item in order_item_details if item])
        #         print (order_item_details)
        #     except:
        #         order_item_details = order_item_details_raw
        try:
            with transaction.atomic():
                # create orderItem of the selected product
                
                # TODO: have changed to create from get_or_create to fix bug with order items deleting if both users have the same order_item in cart... but this spoil the server db, so optimizations recomended
                order_item = OrderItem.objects.create(product=product, nmb=product_quantity, details=order_item_details_raw)
                if order_item:
                    messages.info(request, _("item added to cart"))
                # create order associated with the user
                user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
                user_order.items.add(order_item)
                if status:
                    # generate a reference code
                    user_order.ref_code = generate_order_id()
                    user_order.save()
        except IntegrityError:
            print('IntegrityError')
            raise
        # print(order_item)
        # print(user_order.owner)
        # print(request.POST)
        # print(request.user.is_authenticated)
        # show confirmation message and redirect back to the same page
        # product_id = kwargs.get('item_id')
        # playing with ajax VVV
        # return redirect(reverse('product:product_detail', kwargs={'product_id': product_id}))

        django_messages = dict()

        for message in messages.get_messages(request):
            django_messages.update({
            "level": message.level,
            "message": message.message,
            "extra_tags": message.tags,
            })

        print('SMS', django_messages)

        return_data.update({'amount':request.user.profile.orders.filter(is_ordered=False)[0].items.count() or 0, 'messages':django_messages, 'authenticated': True})
    else:
        return_data.update({ 'authenticated': False })
    return JsonResponse(return_data)

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, _("Item has been deleted"))
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    if request.method == 'POST':
        form = OrderContactPhoneForm(request.POST, instance=existing_order)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            print(request.POST)
            return redirect(reverse('shopping_cart:update_records'))  
    else:
        form = OrderContactPhoneForm()
    context = {
        'order':existing_order,
        'form':form
    }
    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def update_transaction_records(request):
    # get the order being processed
    order_to_purchase = get_user_pending_order(request)

    # update the placed order
    order_to_purchase.customer_email = request.user.email or None
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.is_ordered = True
    order_to_purchase.save()
    
    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.purchases.add(*order_products)
    user_profile.save()
    email_content = generate_success_order_email_content(order_items)


#     datatuple = (
#     (_('PJ | Order accepted!'), 
#     _('''
#     Hi, there!
#     Thank you for ordering:
#     {email_content}
#     We'll contact you again soon.

#     Now you can check out your order #{order_code} details and follow status of your order fulfillment in your awesome PJ-shop profile :)

#     P.S. Have a questions? Contact us, you are always welcome!   
#     ''').format(email_content = email_content, order_code=order_to_purchase.ref_code), 
#     settings.EMAIL_HOST_USER, [order_to_purchase.owner.user.email, settings.DEV_SUPPORT_EMAIL]),

#     (f'New order #{order_to_purchase.ref_code}', 
#     f'''
#     Order #{order_to_purchase.ref_code}:
#     {email_content}
#     Customer contacts: email: {order_to_purchase.owner.user.email}, phone: {order_to_purchase.customer_phone_number}

#     Have a nice day!
#     Και αυτό θα περάσει..
#     ''', 
#     settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,settings.DEV_SUPPORT_EMAIL]),
# )
    subject, from_email, to = _('PJ | Order accepted!'), settings.EMAIL_HOST_USER, settings.DEV_SUPPORT_EMAIL
    text_content = _('''
    Hi, there!
    Thank you for ordering:
    {email_content}
    We'll contact you again soon.

    Now you can check out your order #{order_code} details and follow status of your order fulfillment in your awesome PJ-shop profile :)

    P.S. Have a questions? Contact us, you are always welcome!   
    ''').format(email_content = email_content, order_code=order_to_purchase.ref_code)
    # html_content = f'<html><body>{product_links}</body></html>'
    html_content = render_to_string('order_accepted_email.html', {'order_items': order_items})
    msg_to_castomer = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg_to_castomer.attach_alternative(html_content, "text/html")

    subject, from_email, to = _('PJ | New order!'), settings.EMAIL_HOST_USER, settings.DEV_SUPPORT_EMAIL
    text_content = 'New order, don\'t see order details? Please, inform your developer'
    html_content = render_to_string('new_order.html', {'order_items': order_items, 'order_to_purchase':order_to_purchase})
    msg_to_shop = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg_to_shop.attach_alternative(html_content, "text/html")
    
    try:
        # send_mass_mail(datatuple, fail_silently=False)
        msg_to_castomer.send(fail_silently=False)
        msg_to_shop.send(fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


    
    

    messages.info(request, _("Thank you! Your order accepted!"))
    return redirect(reverse('accounts:my_profile'))
