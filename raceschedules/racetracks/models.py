import geocoder

from django.core.urlresolvers import reverse
from django.contrib.gis.db import models

from localflavor.us.us_states import STATE_CHOICES
from redactor.fields import RedactorField

class Racetrack(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = RedactorField(verbose_name=u'Description', null=True, blank=True)
    street1 = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=33, choices=STATE_CHOICES)
    zip = models.CharField(max_length=32)
    point = models.PointField(srid=4326, null=True, blank=True)
    main_phone = models.BigIntegerField(null=True, blank=True)
    main_email = models.EmailField(max_length=128, null=True, blank=True)
    website = models.URLField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('racetracks:detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        address = self.street1+" "+self.city+" "+self.state+" "+str(self.zip)
        g = geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        self.point = pnt
        super(Racetrack, self).save(*args, **kwargs)

class SurfaceType(models.Model):
    description = models.CharField(max_length=100)
    racetrack = models.ManyToManyField(Racetrack)

    def __str__(self):              # __unicode__ on Python 2
        return self.description

    class Meta:
        ordering = ('description',)
