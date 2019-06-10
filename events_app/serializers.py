from rest_framework import serializers
from .models import Event, Guest


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'image_url',
                  'max_guest_limit', 'moderator_id', 'start_date', 'date_created')

class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'event')
