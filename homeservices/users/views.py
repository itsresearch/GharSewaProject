# users/views.py
from django.shortcuts import render, redirect
from .models import User
import random



def home(request):
    return render(request, 'home.html')
