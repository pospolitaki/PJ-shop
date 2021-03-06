"""hand_made_ishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from product import views

#django-rest
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
#django-rest^

app_name = 'product'
#case1
# urlpatterns = [
#     url(r'^product/(?P<product_id>[\d]+)$', views.product_detail, name='product_detail'),
#     url(r'^product/rest$', views.ProductList.as_view(), name='product_rest'),

# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

#case2
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^product/(?P<product_id>[\d]+)$', views.product_detail, name='product_detail'),
    url(r'^', include(router.urls)),#rest
]