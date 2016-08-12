from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from raceschedules.activities.models import Activity
from .permissions import IsUserOrReadOnly
from .serializers import ActivitySerializer

# Create your views here.
class ActivityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Retrives Events
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (IsUserOrReadOnly,)
