from rest_framework import viewsets, mixins
from . import models
from . import serializers

class BasePrecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BasePreco to be viewed or edited.
    """
    queryset = models.BasePreco.objects.all()
    serializer_class = serializers.BasePrecoSerializer

class CompetitividadeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Competitividade to be viewed or edited.
    """
    queryset = models.Competitividade.objects.all()
    serializer_class = serializers.CompetitividadeSerializer

class ElasticidadeDemandaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ElasticidadeDemanda to be viewed or edited.
    """
    queryset = models.ElasticidadeDemanda.objects.all()
    serializer_class = serializers.ElasticidadeDemandaSerializer

class EttprdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ettprd to be viewed or edited.
    """
    queryset = models.Ettprd.objects.all()
    serializer_class = serializers.EttprdSerializer

class MetasdiariasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Metasdiarias to be viewed or edited.
    """
    queryset = models.Metasdiarias.objects.all()
    serializer_class = serializers.MetasdiariasSerializer

class MovetqViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movetq to be viewed or edited.
    """
    queryset = models.Movetq.objects.all()
    serializer_class = serializers.MovetqSerializer

class MovplncmpcalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movplncmpcal to be viewed or edited.
    """
    queryset = models.Movplncmpcal.objects.all()
    serializer_class = serializers.MovplncmpcalSerializer

class MovvbsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movvbs to be viewed or edited.
    """
    queryset = models.Movvbs.objects.all()
    serializer_class = serializers.MovvbsSerializer

class MovvndhstfimViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movvndhstfim to be viewed or edited.
    """
    queryset = models.Movvndhstfim.objects.all()
    serializer_class = serializers.MovvndhstfimSerializer

class OutputPlnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OutputPln to be viewed or edited.
    """
    queryset = models.OutputPln.objects.all()
    serializer_class = serializers.OutputPlnSerializer

class PrdsmlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Prdsml to be viewed or edited.
    """
    queryset = models.Prdsml.objects.all()
    serializer_class = serializers.PrdsmlSerializer