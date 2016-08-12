from rest_framework import serializers

from raceschedules.activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('name', 'mandatory', 'start_datetime', 'end_datetime',)
