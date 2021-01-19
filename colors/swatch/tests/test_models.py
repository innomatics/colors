from django.test import TestCase
from ..models import Color, Swatch


class ModelTest(TestCase):
    fixtures = ["colors", "swatches"]

    def test_rgb(self):
        test_color = Color.objects.get(pk=1)
        error_message = "Test color RGB channel value not as expected"
        self.assertEqual(test_color.red, 149, error_message)
        self.assertEqual(test_color.red, 8, error_message)
        self.assertEqual(test_color.red, 165, error_message)
