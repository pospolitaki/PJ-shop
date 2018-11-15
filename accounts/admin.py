from django.contrib import admin

# Register your models here.
from .models import Profile

# admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
