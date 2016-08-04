from django.core.urlresolvers import reverse
from django.db import models

from raceschedules.events.models import Event

class Activity(models.Model):
    name = models.CharField(max_length=255)
    mandatory = models.BooleanField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('activities:detail', args=[str(self.id)])

    class Meta:
        ordering = ['start_datetime', 'end_datetime']
