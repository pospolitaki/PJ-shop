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
from landing import urls as landing_urls
from product import urls as product_urls
from order import urls as order_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(landing_urls, namespace='landing')),
    url(r'^', include(product_urls, namespace='product')),
    url(r'^', include(order_urls, namespace='order')),
    url(r'^accounts/', include('allauth.urls', namespace='allauth')),
    url(r'^/', include('allauth.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart')),

] \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
