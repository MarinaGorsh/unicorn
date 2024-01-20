import email
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
