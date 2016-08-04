from django.core.urlresolvers import reverse
from django.db import models

from redactor.fields import RedactorField

from raceschedules.racetracks.models import Racetrack


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RedactorField(verbose_name=u'Description', null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    website = models.URLField(max_length=128, null=True, blank=True)
    racetrack = models.ForeignKey(Racetrack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:detail', args=[str(self.id)])
