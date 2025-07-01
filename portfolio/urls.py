from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('projects/',views.projects,name='projects'),
    path('resume/', views.resume, name='resume'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]
