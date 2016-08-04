from django import forms
from .models import Event

from raceschedules.common.forms import BaseForm


class EventForm(BaseForm):
    class Meta:
        model = Event
        fields = ['name', 'racetrack']
