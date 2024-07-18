from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.TextField(max_length=3000) # roughly 430-750 words
    description = models.TextField(max_length=3000)
    picture = models.CharField()

    def __str__(self):
        return str(self.name)

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    description = models.TextField(max_length=3000) # roughly 430-750 words
    isIndoors = models.BooleanField()

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venues')
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists')
    entry_fee = models.FloatField()

    def __str__(self):
        return str(self.name)