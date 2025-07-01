from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm

def splash(request):
    return render(request, 'splash.html')

def home(request):
    return render(request,"home.html")

def projects(request):
    return render(request,"projects.html")

def resume(request):
    return render(request,"resume.html")

def submit_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully!")
            return redirect('home')  # Make sure 'home' is the correct name of your homepage URL
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
