from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fleet,  name="fleet"),
   # path('about/', views.about, name="about"),
   # path('services/', views.services, name="services"),
   # path('contact/', views.contact, name="contact"),

]
