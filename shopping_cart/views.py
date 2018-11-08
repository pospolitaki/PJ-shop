from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile
from product.models import Product

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order, Transaction

from shopping_cart.forms import OrderContactPhoneForm

from django.http import JsonResponse
from django.db import IntegrityError, transaction

import datetime
import json


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


# @login_required() #fixing ajax + login_requiered cooperating
def add_to_cart(request, **kwargs):
    return_data = dict()

    if request.user.is_authenticated():
    # get the user profile
        user_profile = get_object_or_404(Profile, user=request.user)
        # filter products by id

        product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

        product_quantity = int(request.POST.get('quantity')) or 1 
        try:
            with transaction.atomic():
                # create orderItem of the selected product
                
                # TODO: have changed to create from get_or_create to fix bug with order items deleting if both users have the same order_item in cart... but this spoil the server db, so optimizations recomended
                order_item = OrderItem.objects.create(product=product, nmb=product_quantity)
                # create order associated with the user
                user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
                user_order.items.add(order_item)
                if status:
                    # generate a reference code
                    user_order.ref_code = generate_order_id()
                    user_order.save()
                    messages.info(request, "item added to cart")
        except IntegrityError:
            print('Please, say to your developer that he is loser')
            raise
        print(order_item)
        print(user_order.owner)
        print(request.POST)
        print(request.user.is_authenticated)
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

        return_data.update({'amount':request.user.profile.orders.filter(is_ordered=False)[0].items.count() or 0, 'messages':django_messages, 'authenticated': True})
    else:
        return_data.update({ 'authenticated': False })
    return JsonResponse(return_data)

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
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
        print('THIS IS AN EXISTING ORDER >>>', existing_order)
        form = OrderContactPhoneForm(request.POST, instance=existing_order)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            print('CHECK OUT! THANKS GOD!')
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
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
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

    
    # create a transaction
    transaction = Transaction(profile=request.user.profile,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)
    # save the transcation (otherwise doesn't exist)
    transaction.save()


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Thank you! Your purchase was successful!")
    return redirect(reverse('accounts:my_profile'))


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'shopping_cart/purchase_success.html', {})
