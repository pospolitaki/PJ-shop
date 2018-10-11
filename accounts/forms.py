from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')

        if username == 'kirillos':
            raise forms.ValidationError("hi, kirill!")
        return super().clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
