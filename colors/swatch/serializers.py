from rest_framework import serializers
from .models import Swatch, Color


class SRGBColorSerializer(serializers.ModelSerializer):
    """
    For transporting color data in SRGB format
    """

    class Meta:
        model = Color
        fields = ["red", "blue", "green"]


class HSLColorSerializer(serializers.ModelSerializer):
    """
    For transporting color data in HSL format
    """

    hue = serializers.DecimalField(
        source="hsl.hue", max_digits=5, decimal_places=2
    )
    saturation = serializers.DecimalField(
        source="hsl.saturation", max_digits=5, decimal_places=4
    )
    lightness = serializers.DecimalField(
        source="hsl.lightness", max_digits=5, decimal_places=4
    )

    class Meta:
        model = Color
        fields = ["hue", "saturation", "lightness"]


class SwatchSerializer(serializers.ModelSerializer):
    """
    For transporting swatch data
    """

    srgb_colors = SRGBColorSerializer(many=True, source="colors")
    hsl_colors = HSLColorSerializer(many=True, source="colors")

    class Meta:
        model = Swatch
        fields = ["id", "srgb_colors", "hsl_colors"]
