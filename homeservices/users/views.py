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

def painting(request):
    return render(request, 'service/painting.html')

def plastering(request):
    return render(request, 'service/plastering.html')

def electrical(request):
    return render(request, 'service/electrical.html')

def plumbing(request):
    return render(request, 'service/plumbing.html')

def carpentry(request):
    return render(request, 'service/carpentry.html')

def flooring(request): 
    return render(request, 'service/flooring.html')

def roofing(request):
    return render(request, 'service/roofing.html')

def cleaning(request):
    return render(request, 'service/cleaning.html')

def appliance(request):
    return render(request, 'service/appliance.html')



