from django.conf.urls import *

from rest_framework.routers import DefaultRouter

from .racetracks.views import RacetrackViewSet
from .events.views import EventViewSet
from .activities.views import ActivityViewSet

router = DefaultRouter()
router.register(r'racetracks', RacetrackViewSet)
router.register(r'events', EventViewSet)
router.register(r'activities', ActivityViewSet)
urlpatterns = router.urls
