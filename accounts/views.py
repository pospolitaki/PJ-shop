from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserRegisterForm, UserLoginForm

class UserRegisterFormView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/registration_form.html'
    title = 'Здесь Вы можете зарегестрироваться'
    btn_url = 'landing:register'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form, 'title':self.title, 'btn_url':self.btn_url})

    # process form data into db    
    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():

            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return redirect('landing:home')
        return render(request, self.template_name, {'form':form, 'title':self.title, 'btn_url':self.btn_url})

class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'accounts/registration_form.html'
    title = 'Вход'
    btn_url = 'landing:login'
    next_page = None

    def get(self, request, next_page):
        form = self.form_class(None)
        self.__class__.next_page = next_page
        return render(request, self.template_name, {'form':form, 'title':self.title, 'btn_url':self.btn_url})

    # process form data into db    
    def post(self, request, next_page=''):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return redirect('landing:home')
                    return redirect(self.__class__.next_page)
        return render(request, self.template_name, {'form':form, 'title':self.title, 'btn_url':self.btn_url})

def logout_view(request, next_page):
    logout(request)
    return redirect(next_page)
    

