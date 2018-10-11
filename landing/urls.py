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
from django.conf.urls import url
from django.contrib import admin
from landing import views
from accounts.views import UserRegisterFormView, UserLoginFormView, logout_view

app_name = 'landing'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^categories/(?P<category>[\d]+)$', views.categories_detail, name='categories'),
    #auth v
    url(r'^register$', UserRegisterFormView.as_view(), name='register'),
    url(r'^register/(?P<next_page>.*)$', UserRegisterFormView.as_view(), name='register'),

    url(r'^login/$', UserLoginFormView.as_view(), name='login'),
    url(r'^login/(?P<next_page>.*)/$', UserLoginFormView.as_view(), name='login'),
    url(r'^logout/(?P<next_page>.*)/$', logout_view, name='logout'),
    #auth ^
    url(r'^landing/$', views.landing, name='index'),
    url(r'^practice_1/$', views.practice, name='practice'),
    url(r'^practice_2/$', views.practice2, name='practice2'),

]
