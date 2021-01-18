from random import randint

from django.db import models


class Color(models.Model):
    """
    Stores a 24 bit color in sRGB color space with 8-bit channel data
    """

    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    class Meta:
        indexes = [
            models.Index(
                fields=["red", "blue", "green"], name="channel_data_idx"
            )
        ]


def create_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    obj, _ = Color.objects.get_or_create(red=red, green=green, blue=blue)
    return obj
