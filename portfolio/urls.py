from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('skills/',views.skill,name='skill'),
    path('academics/',views.academics,name='academics'),
    path('projects/',views.projects,name='projects'),
]
