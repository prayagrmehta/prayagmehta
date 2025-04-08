from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def splash(request):
    return render(request, 'splash.html')

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def skill(request):
    return render(request,"skills.html")

def academics(request):
    return render(request,"academics.html")

def projects(request):
    return render(request,"projects.html")

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ["prayagrmehta.1011@gmail.com"],  # Replace with your email
        )
        return redirect("contact")  # Redirect to the contact page after submission