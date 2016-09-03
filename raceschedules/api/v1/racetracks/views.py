from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from raceschedules.racetracks.models import Racetrack
from .permissions import IsUserOrReadOnly
from .serializers import RacetrackSerializer, CreateRacetrackSerializer


class RacetrackViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = Racetrack.objects.all()
    serializer_class = RacetrackSerializer
    permission_classes = (IsUserOrReadOnly,)
    
    def get_queryset(self):
        qs = super().get_queryset()
        distance_filter = self.request.query_params.get('distance_filter', None)
        
        if self.request.user.is_authenticated():
            pnt = self.request.user.userprofile.point
        
            if distance_filter:
                qs= Racetrack.objects.filter(point__distance_lte=(pnt, D(mi=distance_filter))).annotate(distance=Distance('point', pnt)).order_by('distance')
            else:
                qs = Racetrack.objects.annotate(distance=Distance('point', pnt)).order_by('distance')

        return qs