from random import randint
from django.db import models
import colorsys
from django.utils.functional import cached_property


def int8_to_float(int8_val):
    return float(int8_val) / 255.0


def float_to_degrees(float_val):
    return (1 - float_val) * 360.0


class ColorManager(models.Manager):
    """
    Manager of the Color model
    """

    def create_random_color(self):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        obj, _ = Color.objects.get_or_create(red=red, green=green, blue=blue)
        return obj


class Color(models.Model):
    """
    Stores a 24 bit color in sRGB color space with 8-bit channel data
    """

    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    objects = ColorManager()

    class Meta:
        indexes = [
            models.Index(
                fields=["red", "blue", "green"], name="channel_data_idx"
            )
        ]

    @cached_property
    def hsl(self):
        return colorsys.rgb_to_hls(
            int8_to_float(self.red),
            int8_to_float(self.green),
            int8_to_float(self.blue),
        )

    @property
    def hsl_hue(self):
        return float_to_degrees(self.hsl[0])

    @property
    def hsl_lightness(self):
        return self.hsl[1]

    @property
    def hsl_saturation(self):
        return self.hsl[2]
