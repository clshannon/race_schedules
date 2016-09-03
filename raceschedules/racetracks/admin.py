from django.contrib.gis import admin
from .models import Racetrack, SurfaceType

from raceschedules.events.models import Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 5

class RacetrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    inlines = [
       EventInline,
    ]

admin.site.register(Racetrack, RacetrackAdmin)
admin.site.register(SurfaceType)
