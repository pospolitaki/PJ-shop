from __future__ import unicode_literals
from django_easy_currencies.views.ChangeCurrencyView import ChangeCurrencyView
# from django.conf.urls import patterns, url
from django.conf.urls import url


# urlpatterns = patterns(
#     '',
#     url(
#         regex=r'^change/$',
#         view=ChangeCurrencyView.as_view(),
#         name='change_currency'
#     ),
# )
urlpatterns = [
    url(r'^change/$', ChangeCurrencyView.as_view(), name='change_currency'),
]
