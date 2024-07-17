import json

artists = [
    {
        "model": "backend.artist",
        "pk": 1,
        "fields": {
            "name": "Kendrick Lamar",
            "genre": "Hip Hop",
            "description": "An American rapper, songwriter, and record producer."
        }
    },
    {
        "model": "backend.artist",
        "pk": 2,
        "fields": {
            "name": "J. Cole",
            "genre": "Hip Hop",
            "description": "An American rapper, singer, songwriter, and record producer."
        }
    },
    {
        "model": "backend.artist",
        "pk": 3,
        "fields": {
            "name": "Nicki Minaj",
            "genre": "Hip Hop",
            "description": "A Trinidadian-American rapper, singer, and songwriter."
        }
    }
]

venues = [
    {
        "model": "backend.venue",
        "pk": 1,
        "fields": {
            "name": "Madison Square Garden",
            "location": "4 Pennsylvania Plaza, New York, NY 10001",
            "description": "An indoor arena in New York City.",
            "isIndoors": True
        }
    },
    {
        "model": "backend.venue",
        "pk": 2,
        "fields": {
            "name": "Staples Center",
            "location": "1111 S Figueroa St, Los Angeles, CA 90015",
            "description": "A multi-purpose arena in Los Angeles.",
            "isIndoors": True
        }
    }
]

events = [
    {
        "model": "backend.event",
        "pk": 1,
        "fields": {
            "name": "The Championship Tour",
            "venue": 1,
            "artists": 1,
            "entry_fee": 75.0
        }
    },
    {
        "model": "backend.event",
        "pk": 2,
        "fields": {
            "name": "Dreamville Festival",
            "venue": 2,
            "artists": 2,
            "entry_fee": 65.0
        }
    },
    {
        "model": "backend.event",
        "pk": 3,
        "fields": {
            "name": "Nicki WRLD Tour",
            "venue": 1,
            "artists": 3,
            "entry_fee": 85.0
        }
    }
]

with open('artists.json', 'w', encoding='utf-8') as f:
    json.dump(artists, f, indent=4)

with open('venues.json', 'w', encoding='utf-8') as f:
    json.dump(venues, f, indent=4)

with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, indent=4)
