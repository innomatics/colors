from django.test import TestCase
from ..models import Color


class ModelTest(TestCase):
    fixtures = ["colors", "swatches"]

    def test_rgb(self):
        test_color = Color.objects.get(pk=1)
        error_message = "Test color RGB channel value not as expected"
        self.assertEqual(test_color.red, 149, error_message)
        self.assertEqual(test_color.green, 8, error_message)
        self.assertEqual(test_color.blue, 165, error_message)

    def test_hsl(self):
        test_color = Color.objects.get(pk=1)
        error_message = "Test color HSL channel value not as expected"
        self.assertEqual(round(test_color.hsl.hue, 2), 66.11, error_message)
        self.assertEqual(
            round(test_color.hsl.saturation, 3), 0.908, error_message
        )
        self.assertEqual(
            round(test_color.hsl.lightness, 3), 0.339, error_message
        )
