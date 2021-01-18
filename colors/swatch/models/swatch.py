from django.db import models
from .color import Color, create_random_color


class SwatchManager(models.Manager):
    def create_random_swatch(self, numcolors=5):
        colors = []
        for i in range(numcolors):
            colors.append(create_random_color())
        swatch = Swatch.objects.create()
        swatch.colors.set(colors)
        return swatch


class Swatch(models.Model):
    """
    Stores a collection of Colors
    """

    colors = models.ManyToManyField(Color)
    objects = SwatchManager()
