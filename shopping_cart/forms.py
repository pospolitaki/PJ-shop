from django import forms
from django.forms import ModelForm, TextInput
from shopping_cart.models import Order
from django.utils.translation import gettext_lazy as _


class OrderContactPhoneForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_phone_number'] 
        widgets = {
            'customer_phone_number': TextInput(attrs={'placeholder': '+380123456789'}),
        }

    def clean_customer_phone_number(self):
        data = self.cleaned_data["customer_phone_number"]
        if not data:
            raise forms.ValidationError(_("We won't give your phone number to anyone we just need to contact you somehow.."))
        return data
    