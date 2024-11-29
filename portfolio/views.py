import io
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render

skills = [
    {"name": "Web Development", "proficiency": 85},
    {"name": "Data Science", "proficiency": 80},
    {"name": "Cybersecurity", "proficiency": 70},
    {"name": "Cloud Computing", "proficiency": 75},
    {"name": "AI & ML", "proficiency": 60},
    {"name": "Programming", "proficiency": 90},
]

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