# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import geocoder

from localflavor.us.us_states import STATE_CHOICES
from redactor.fields import RedactorField

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
    
    
class UserProfile(gismodels.Model):
    
    user = gismodels.OneToOneField(User, unique=True)
    description = RedactorField(verbose_name=u'Description', null=True, blank=True)
    street1 = models.CharField(max_length=128, null=True, blank=True)
    street2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=33, choices=STATE_CHOICES, null=True, blank=True)
    zip = models.CharField(max_length=32)
    point = gismodels.PointField(srid=4326, null=True, blank=True)
    
    REQUIRED_FIELDS = ('user',)
    
    def save(self, *args, **kwargs):
        g = geocoder.google(str(self.zip))
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        self.point = pnt
        super(UserProfile, self).save(*args, **kwargs)