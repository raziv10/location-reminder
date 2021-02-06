from django.db import models

# Create your models here.


class location(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Demo')
    # slug = models.SlugField(unique=True, blank=True)
    task = models.CharField(max_length=500, blank=False, default='Explore')
    longitude = models.CharField(
        max_length=100, blank=False, default='85.32608415708333')
    latitude = models.CharField(
        max_length=100, blank=False, default='27.70885940768541')

    def __str__(self):
        return '{}, {}'.format(self.name, self.task)
