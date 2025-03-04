from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'users/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error in signup process')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def appointment(request):
    return render(request, 'appointment.html')

def feature(request):
    return render(request, 'feature.html')

def contact(request):
    return render(request, 'contact.html')