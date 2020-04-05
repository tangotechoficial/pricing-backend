from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Campo, Sequencia, Camada, TipoValor, ChaveContas, Condicao, EsquemaDeCalculo, CondicaoCamadaEsquema, SequenciaCondicao
from .serializer import CampoSerializer, SequenciaSerializer, CamadaSerializer, TipoValorSerializer, ChaveContasSerializer, CondicaoSerializer, EsquemaDeCalculoSerializer, CondicaoCamadaEsquemaSerializer, SequenciaCondicaoSerializer


""" class SEQ_CAMPOViewSet(viewsets.ModelViewSet):
    queryset = SEQ_CAMPO.objects.all()
    serializer_class = SEQ_CAMPOSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='last',
        url_name='last',
    )
    def get_last_seqcampo(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs) """

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

class ChaveContasViewSet(viewsets.ModelViewSet):
    queryset = ChaveContas.objects.all()
    serializer_class = ChaveContasSerializer

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
"""
class CAMADACONDViewSet(viewsets.ModelViewSet):
    queryset = CAMADA.objects.all()
    serializer_class = CAMADACONDSerializer

class CONDICAOSEQViewSet(viewsets.ModelViewSet): 
    queryset = CONDICAO.objects.all()
    serializer_class = CONDICAOSEQSerializer

class CONDICAOViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO.objects.all()
    serializer_class = CONDICAOSerializer

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
    

class CONDICAO_SEQUENCIAViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO_SEQUENCIA.objects.all()
    serializer_class = CONDICAO_SEQUENCIASerializer

class ESQUEMA_DE_CALCULOViewSet(viewsets.ModelViewSet):
    queryset = ESQUEMA_DE_CALCULO.objects.all()
    serializer_class = ESQUEMA_DE_CALCULOSerializer

class PRECOViewSet(viewsets.ModelViewSet):
    queryset = PRECO.objects.all()
    serializer_class = PRECOSerializer

class CONDICAO_CAMADA_ESQUEMAViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO_CAMADA_ESQUEMA.objects.all()
    serializer_class = CONDICAO_CAMADA_ESQUEMASerializer

class MERCADORIAViewSet(viewsets.ModelViewSet):
    queryset = MERCADORIA.objects.all()
    serializer_class = MERCADORIASerializer

class FILIALViewSet(viewsets.ModelViewSet):
    queryset = FILIAL.objects.all()
    serializer_class = FILIALSerializer

class FATURAMENTOViewSet(viewsets.ModelViewSet):
    queryset = FATURAMENTO.objects.all()
    serializer_class = FATURAMENTOSerializer

class ESTADOViewSet(viewsets.ModelViewSet):
    queryset = ESTADO.objects.all()
    serializer_class = ESTADOSerializer

class REGIONViewSet(viewsets.ModelViewSet):
    queryset = REGION.objects.all()
    serializer_class = REGIONSerializer
 """