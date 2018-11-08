from django import forms
from django.forms import ModelForm
from shopping_cart.models import Order

class OrderContactPhoneForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_phone_number']

    def clean_customer_phone_number(self):
        data = self.cleaned_data["customer_phone_number"]
        if not data:
            raise forms.ValidationError("We won't give your phone number to anyone we just need to contact you somehow..")
        return data
    