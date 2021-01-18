from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Swatch
from .serializers import SwatchSerializer


def get_new_swatch(request):
    new_swatch = Swatch.objects.create_random_swatch()
    serializer = SwatchSerializer(new_swatch)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type="application/json")


class SwatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows swatches to be viewed or edited.
    """

    queryset = Swatch.objects.all()
    serializer_class = SwatchSerializer
