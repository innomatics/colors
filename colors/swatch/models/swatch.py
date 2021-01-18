from django.db import models
from .color import Color


class Swatch(models.Model):
    """
    Stores a collection of Colors
    """

    colors = models.ManyToManyField(Color)
