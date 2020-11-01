from django.shortcuts import render
from .models import Team

# Create your views herde.

def home(request):
    teams = Team.objects.all()
    data = {
       "teams": teams,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
       "teams": teams,
    }
    return render(request, 'pages/about.html', data)

def test(request):
    return render(request, 'test.html' )

def services(request):
    return render(request, 'pages/services.html' )

def contact(request):
    return render(request, 'pages/contact.html' )
