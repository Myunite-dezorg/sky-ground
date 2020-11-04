# from modelclone import ClonableModelAdmin
from django.contrib import admin
from .models import Aircraft, AircraftSpec, AircraftDimensions, AircraftPerfomance, AircraftCapacity, AircraftEngines
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
@admin.register(AircraftDimensions)
class AircraftDimensionsAdmin(admin.ModelAdmin):
         save_as = True
         list_display = ('type', )
@admin.register(AircraftPerfomance)
class AircraftPerfomanceAdmin(admin.ModelAdmin):
         save_as = True
         list_display = ('type', )
@admin.register(AircraftCapacity)
class AircraftCapacityAdmin(admin.ModelAdmin):
         save_as = True
         list_display = ('type', )
@admin.register(AircraftEngines)
class AircraftEnginesAdmin(admin.ModelAdmin):
         save_as = True
         list_display = ('type', )
