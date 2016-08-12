from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from raceschedules.events.models import Event
from .permissions import IsUserOrReadOnly
from .serializers import EventSerializer

# Create your views here.
class EventViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Retrives Events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsUserOrReadOnly,)
