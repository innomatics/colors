from rest_framework import viewsets
from .models import Swatch
from .serializers import SwatchSerializer


class SwatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows swatches to be viewed or edited.
    """

    queryset = Swatch.objects.all()
    serializer_class = SwatchSerializer
