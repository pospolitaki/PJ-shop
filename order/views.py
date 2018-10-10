from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm 


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    print (session_key)

    return_dict.update({1:'hallo'})
    # data = request.POST
    # product_id = data.get("product_id")
    # quantity = data.get("quantity")

    return JsonResponse(return_dict)

class UserFormView(View):
    form_class = UserForm
    template_name = 'order/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data into db    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('landing:home')
        return render(request, self.template_name, {'form':form})