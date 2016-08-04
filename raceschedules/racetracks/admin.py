from django.contrib import admin
from .models import Racetrack, SurfaceType

from raceschedules.events.models import Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 5

class RacetrackAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]

admin.site.register(Racetrack, RacetrackAdmin)
admin.site.register(SurfaceType)
