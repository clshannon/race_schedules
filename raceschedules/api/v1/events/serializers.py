from rest_framework import serializers

from raceschedules.events.models import Event
from raceschedules.api.v1.activities.serializers import ActivitySerializer


class EventSerializer(serializers.ModelSerializer):
    activity_set = ActivitySerializer(many=True)

    class Meta:
        model = Event
        fields = ('name', 'description', 'start_datetime', 'end_datetime', 'website', 'activity_set',)
