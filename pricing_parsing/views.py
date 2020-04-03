from rest_framework import viewsets, mixins
from . import models
from . import serializers

class MovplncmpcalViewSet(viewsets.ModelViewSet):
    queryset = models.Movplncmpcal.objects.all()
    serializer_class = serializers.MovplncmpcalSerializer
