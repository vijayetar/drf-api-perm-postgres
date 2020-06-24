from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

	#this is where you would put in the checks
	# def

class LogoutView(TemplateView):
	template_name = 'logout.html'