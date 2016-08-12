from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

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
