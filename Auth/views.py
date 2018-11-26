from django.http import response, HttpResponse

from Auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/user/login'
    template_name = 'registration/register.html'
