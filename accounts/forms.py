from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
    authenticate,

)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='e-mail')
    email2 = forms.EmailField(label='Подтвердите e-mail')


    class Meta:
        model = User
        fields = ['username', 'email','email2', 'password']

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2') #order is important - comes through only in this order
        if email != email2:
            raise forms.ValidationError("адреса не совпадают")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('такой e-mail уже зарегестрирван')
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Что-то не так')
            if not user.check_password(password):
                raise forms.ValidationError('Возможно Вы ошиблись')
            if not user.is_active:
                raise forms.ValidationError('Данный пользователь неактивен')
        return super().clean(*args, **kwargs)



