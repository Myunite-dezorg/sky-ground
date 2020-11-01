from django.shortcuts import render

# Create your views here.
def fleet(request):
    return render(request, 'fleet/fleet.html')
