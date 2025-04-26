from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class     = UserCreationForm
    template_name  = 'authentication/signup.html'
    success_url    = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

class HomeView(TemplateView):
    template_name = 'authentication/homepage.html'