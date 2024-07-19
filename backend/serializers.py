from rest_framework import serializers
from .models import Venue, Artist, Event

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'genre', 'description', 'picture']

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id', 'name', 'location', 'description', 'isIndoors']

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    artists = ArtistSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'venue', 'artists', 'entry_fee']
