from django.contrib import admin
from landing.models import Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_editable = ('name', 'email')
    search_fields = ('name',)

admin.site.register(Subscriber, SubscriberAdmin)