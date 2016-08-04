from django.contrib import admin

from .models import Event
from raceschedules.activities.models import Activity

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 10

class EventAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline,
    ]

admin.site.register(Event, EventAdmin)
