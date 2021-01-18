from rest_framework import serializers
from .models import Swatch, Color


class ColorSerializer(serializers.ModelSerializer):
    """
    For transporting color data
    """

    class Meta:
        model = Color
        fields = ["red, blue, green"]


class SwatchSerializer(serializers.Serializer):
    """
    For transporting swatch data
    """

    class Meta:
        model = Swatch
        colors = ColorSerializer(many=True)
