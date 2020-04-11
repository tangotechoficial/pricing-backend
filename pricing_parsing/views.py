from rest_framework import viewsets, mixins
from . import models
from . import serializers
from . import pagination
from django_filters.rest_framework import DjangoFilterBackend

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

class EttprdFilterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ettprd to be viewed or edited.
    """
    queryset = models.Ettprd.objects.all()
    serializer_class = serializers.EttprdFilterSerializer

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
    pagination_class = pagination.StandardResultsSetPagination

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

class DadosMestre_VerbaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre_Verba to be viewed or edited.
    """
    queryset = models.DadosMestre_Verba.objects.all()
    serializer_class = serializers.DadosMestre_VerbaSerializer
    pagination_class = pagination.StandardResultsSetPagination

class ElasticidadeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Elasticidade to be viewed or edited.
    """
    queryset = models.Elasticidade.objects.all()
    serializer_class = serializers.ElasticidadeSerializer

class VerbaeBCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows VerbaeBC to be viewed or edited.
    """
    queryset = models.VerbaeBC.objects.all()
    serializer_class = serializers.VerbaeBCSerializer

class VendasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Vendas to be viewed or edited.
    """
    queryset = models.Vendas.objects.all()
    serializer_class = serializers.VendasSerializer

class DadosMestre_ComposicaoPrecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre_ComposicaoPreco to be viewed or edited.
    """
    queryset = models.DadosMestre_ComposicaoPreco.objects.all()
    serializer_class = serializers.DadosMestre_ComposicaoPrecoSerializer
    pagination_class = pagination.StandardResultsSetPagination

class DiretrizesEstrategicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.all()
    serializer_class = serializers.DiretrizesEstrategicaSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['DESDRTCLLATU', 'CODGRPMER', 'DESGRPMER', 'CODFMLMER', 'DESFMLMER',
                  'CODCLSMER', 'DESCLSMER', 'CODDIVFRN', 'NOMFRN', 'CODFIL', 'CODESTUNI', ]

class DiretrizesFilterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.all()
    serializer_class = serializers.DiretrizesFilterSerializer
    pagination_class = pagination.StandardResultsSetPagination

class DiretrizesFilterDirectoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.distinct('DESDRTCLLATU')
    serializer_class = serializers.DiretrizesFilterDirectoriesSerializer
    pagination_class = pagination.StandardResultsSetPagination

class DiretrizesFilterGroupMerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.distinct('CODGRPMER')
    serializer_class = serializers.DiretrizesFilterGroupMerSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['DESDRTCLLATU']

class DiretrizesFilterCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.distinct('CODFLMMER')
    serializer_class = serializers.DiretrizesFilterCategorySerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['CODGRPMER']

class DiretrizesFilterSubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.distinct('CODCLSMER')
    serializer_class = serializers.DiretrizesFilterSubCategorySerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['CODFLMMER']
    

class PlanoComprasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlanoCompras to be viewed or edited.
    """
    queryset = models.PlanoCompras.objects.all()
    serializer_class = serializers.PlanoComprasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['CODESTUNI', 'CODFILEPD', 'CODFILFAT', 'CODPRD']


