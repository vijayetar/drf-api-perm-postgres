from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class LogoutView(TemplateView):
	template_name = 'logout.html'