from rest_framework import serializers
from .models import Swatch, Color


class ColorSerializer(serializers.ModelSerializer):
    """
    For transporting color data
    """

    class Meta:
        model = Color
        fields = ["red", "blue", "green"]


class SwatchSerializer(serializers.ModelSerializer):
    """
    For transporting swatch data
    """

    colors = ColorSerializer(many=True)

    class Meta:
        model = Swatch
        fields = "__all__"
