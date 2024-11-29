from django.shortcuts import render,HttpResponse

def splash(request):
    return render(request, 'splash.html')

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def skills(request):
    return render(request,"skills.html")

def academics(request):
    return render(request,"academics.html")