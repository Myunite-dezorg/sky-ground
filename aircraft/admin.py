# from modelclone import ClonableModelAdmin
from django.contrib import admin
from .models import Aircraft, AircraftSpec
from django.utils.html import format_html


# Register your models here.
@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
     save_as = True
     list_display = ('id','manufacture', 'title', 'family',  )





@admin.register(AircraftSpec)
class AircraftSpecAdmin(admin.ModelAdmin):
     save_as = True
     list_display = ('type', )
