from django.shortcuts import render

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