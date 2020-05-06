from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core import serializers;
from .models import Campo, Sequencia, CampoSequencia, TipoValor, Camada, Condicao, SequenciaCondicao, EsquemaDeCalculo, CondicaoCamadaEsquema, Preco, Mercadoria
from .serializer import CampoSerializer, SequenciaSerializer, CampoSequenciaSerializer, TipoValorSerializer, CamadaSerializer, CondicaoSerializer, SequenciaCondicaoSerializer, EsquemaDeCalculoSerializer, CondicaoCamadaEsquemaSerializer, PrecoSerializer, MercadoriaSerializer

class CampoSequenciaViewSet(viewsets.ModelViewSet):
    queryset = CampoSequencia.objects.all()
    serializer_class = CampoSequenciaSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='last',
        url_name='last',
    )
    def get_last_seqcampo(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs)

class MercadoriaViewSet(viewsets.ModelViewSet):
    model = Mercadoria
    queryset = Mercadoria.objects.all()
    serializer_class = MercadoriaSerializer

    def list(self, request):
        queryset = Mercadoria.objects.raw('''SELECT * FROM (SELECT CODEMP || CODMER AS ID, CODMER, DESMER FROM MRT.T0100086 WHERE T0100086.DESMER != %s) WHERE ROWNUM <= %s''', ["-", 50])
        serializer = MercadoriaSerializer(queryset, many=True)
        return Response(serializer.data)

class CampoViewSet(viewsets.ModelViewSet):
    queryset = Campo.objects.all()
    serializer_class = CampoSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='last',
        url_name='last',
    )
    def get_last_campo(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs)


class SequenciaViewSet(viewsets.ModelViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='last',
        url_name='last',
    )
    def get_last_sequencia(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs)

class TipoValorViewSet(viewsets.ModelViewSet):
    queryset = TipoValor.objects.all()
    serializer_class = TipoValorSerializer

class CamadaViewSet(viewsets.ModelViewSet):
    queryset = Camada.objects.all()
    serializer_class = CamadaSerializer

class CondicaoViewSet(viewsets.ModelViewSet): 
    queryset = Condicao.objects.all()
    serializer_class = CondicaoSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='last',
        url_name='last',
    )
    def get_last_condicao(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs)

class SequenciaCondicaoViewSet(viewsets.ModelViewSet):
    queryset = SequenciaCondicao.objects.all()
    serializer_class = SequenciaCondicaoSerializer

class EsquemaDeCalculoViewSet(viewsets.ModelViewSet):
    queryset = EsquemaDeCalculo.objects.all()
    serializer_class = EsquemaDeCalculoSerializer

class CondicaoCamadaEsquemaViewSet(viewsets.ModelViewSet):
    queryset = CondicaoCamadaEsquema.objects.all()
    serializer_class = CondicaoCamadaEsquemaSerializer

class PrecoViewSet(viewsets.ModelViewSet):
    queryset = Preco.objects.all()
    serializer_class = PrecoSerializer

""" class ChaveContasViewSet(viewsets.ModelViewSet):
    queryset = ChaveContas.objects.all()
    serializer_class = ChaveContasSerializer

    class FilialExpedicaoViewSet(viewsets.ModelViewSet):
        queryset = FilialExpedicao.objects.all()
        serializer_class = FilialExpedicaoSerializer

    class FilialFaturamentoViewSet(viewsets.ModelViewSet):
        queryset = FilialFaturamento.objects.all()
        serializer_class = FilialFaturamentoSerializer

    class RegiaoViewSet(viewsets.ModelViewSet):
        queryset = Regiao.objects.all()
        serializer_class = RegiaoSerializer

    class EstadoViewSet(viewsets.ModelViewSet):
        queryset = Estado.objects.all()
        serializer_class = EstadoSerializer

    class MercadoriaViewSet(viewsets.ModelViewSet):
        queryset = Mercadoria.objects.all()
        serializer_class = MercadoriaSerializer

    class ChavePrecificaoViewSet(viewsets.ModelViewSet):
        queryset = ChavePrecificao.objects.all()
        serializer_class = ChavePrecificaoSerializer

    class EsquemaRelationViewSet(viewsets.ModelViewSet):
        queryset = EsquemaDeCalculo.objects.all()
        serializer_class = EsquemaRelationSerializer

    class CodterchvCodcnlViewSet(viewsets.ModelViewSet):
        queryset = CodterchvCodcnl.objects.all()
        serializer_class = CodterchvCodcnlSerializer   """