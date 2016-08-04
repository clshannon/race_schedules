from django import forms
from .models import Racetrack

from raceschedules.common.forms import BaseForm

class RacetrackForm(BaseForm):
    class Meta:
        model = Racetrack
        fields = ['name', 'street1', 'street2', 'city', 'state', 'zip', 'website']
