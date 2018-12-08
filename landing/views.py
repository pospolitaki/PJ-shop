from django.shortcuts import render
from landing.forms import SubscriberForm
from product.models import *
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def landing(request):
    subscriber_form = SubscriberForm(request.POST or None)

    print(subscriber_form.is_valid())
    print(subscriber_form.data)
    if request.method == 'GET':
        return render(request, 'landing/landing_.html', locals())

    elif request.method == "POST" and subscriber_form.is_valid():
        subscriber_form.save()
        return redirect(reverse('landing:index'))
    else:
        return HttpResponse(status=405)
        
def home(request):
    categories = Category.objects.prefetch_related('products__product_imgs').filter(is_active=True).order_by('-id')
    products_for_children = Product.objects.filter(for_children=True)
    return render(request, 'landing/home_categories.html', locals())

def welcome(request):
    return render(request, 'landing/welcome.html')

def categories_detail(request, category):
    if int(category):
        category = Category.objects.filter(id=category).first()
        products_images = ProductImage.objects.select_related('product').filter(is_active=True, is_main=True, product__category=category,product__for_children=False, product__is_active=True)
    else:
        category = {'name':_('For children')}
        products_images = ProductImage.objects.select_related('product').filter(is_active=True, is_main=True, product__for_children=True, product__is_active=True)
    return render(request, 'landing/categories_detail.html', locals())

    
    