from django.shortcuts import render

# Create your views herd         e.

def home(request):
    return render(request, 'pages/home.html')
