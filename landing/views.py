from django.shortcuts import render
from landing.forms import SubscriberForm
from product.models import *
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def landing(request):

    #works fine
    # if request.method == "GET":
    #     subscriber_form = SubscriberForm()

    #     return render(request, 'landing/landing.html', locals())
    
    # elif request.method =="POST":
    #     subscriber_form = SubscriberForm(request.POST)
    #     if subscriber_form.is_valid():
    #         subscriber_form.save()
    #         return redirect(reverse('landing:index'))
    # return HttpResponse(status=405)
       
    subscriber_form = SubscriberForm(request.POST or None)

    print(subscriber_form.is_valid())
    print(subscriber_form.data)
    if request.method == 'GET':
        return render(request, 'landing/landing_.html', locals())
        # output = _('hallo')
        # return HttpResponse(output)

    elif request.method == "POST" and subscriber_form.is_valid():
        subscriber_form.save()
        return redirect(reverse('landing:index'))
    else:
        return HttpResponse(status=405)
        
def home(request):
    categories = Category.objects.all().order_by('name')
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, 'landing/home_categories.html', locals())

def practice(request):
    return render(request, 'landing/practice_1.html')

def practice2(request):
    return render(request, 'landing/practice_2.html')

def welcome(request):
    return render(request, 'landing/welcome.html')


def categories_detail(request, category):
    category = Category.objects.filter(id=category).first()
    products_images = ProductImage.objects.select_related('product').filter(is_active=True, is_main=True, product__category=category, product__is_active=True)

    return render(request, 'landing/categories_detail.html', locals())

    
    