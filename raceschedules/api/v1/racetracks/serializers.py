from rest_framework import serializers

from raceschedules.racetracks.models import Racetrack, SurfaceType
from raceschedules.api.v1.events.serializers import EventSerializer

class RacetrackSerializer(serializers.ModelSerializer):
    surfacetype_set = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')
    event_set = EventSerializer(many=True)
    #event_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Racetrack
        fields = ('name', 'description', 'street1', 'street2', 'city', 'state', 'main_phone', 'main_email', 'website', 'surfacetype_set', 'event_set')


class CreateRacetrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Racetrack
        fields = ('name', 'description', 'street1', 'street2', 'city', 'state', 'main_phone', 'main_email', 'website')


class SurfaceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurfaceType
        fields = ('description')
