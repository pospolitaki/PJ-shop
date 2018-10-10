from django import forms
from landing.models import Subscriber

from django.contrib.auth.models import User
from django import forms

# class SubscriberForm(forms.ModelForm):

#     class Meta:
#         model = Subscriber
#         exclude = ['id']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    