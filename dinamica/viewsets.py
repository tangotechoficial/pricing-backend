from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SEQ_CAMPO, SEQUENCIA, SEQ_AUX, CHAVE_CONTAS, TIPOVALOR, CAMADA, CONDICAO, CONDICAO_SEQUENCIA, CONDICAO_CAMADA, CANAL_VENDAS, LINHA_NEGOCIO, ESQUEMA_DE_CALCULO, CAMADA_ESQUEMA, PRECO
from .serializer import SEQ_CAMPOSerializer, SEQUENCIASerializer, SEQ_AUXSerializer, CHAVE_CONTASSerializer, TIPOVALORSerializer, CAMADASerializer, CONDICAOSerializer, CONDICAO_SEQUENCIASerializer, CONDICAO_CAMADASerializer, CANAL_VENDASSerializer, LINHA_NEGOCIOSerializer, ESQUEMA_DE_CALCULOSerializer, CAMADA_ESQUEMASerializer, PRECOSerializer


class SEQ_CAMPOViewSet(viewsets.ModelViewSet):
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
        return self.retrieve(request, *args, **kwargs)


class SEQUENCIAViewSet(viewsets.ModelViewSet):
    queryset = SEQUENCIA.objects.all()
    serializer_class = SEQUENCIASerializer

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

class SEQ_AUXViewSet(viewsets.ModelViewSet):
    queryset = SEQ_AUX.objects.all()
    serializer_class = SEQ_AUXSerializer

class CHAVE_CONTASViewSet(viewsets.ModelViewSet):
    queryset = CHAVE_CONTAS.objects.all()
    serializer_class = CHAVE_CONTASSerializer

class TIPOVALORViewSet(viewsets.ModelViewSet):
    queryset = TIPOVALOR.objects.all()
    serializer_class = TIPOVALORSerializer

class CAMADAViewSet(viewsets.ModelViewSet):
    queryset = CAMADA.objects.all()
    serializer_class = CAMADASerializer

class CONDICAOViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO.objects.all()
    serializer_class = CONDICAOSerializer

class CONDICAO_SEQUENCIAViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO_SEQUENCIA.objects.all()
    serializer_class = CONDICAO_SEQUENCIASerializer

class CONDICAO_CAMADAViewSet(viewsets.ModelViewSet):
    queryset = CONDICAO_CAMADA.objects.all()
    serializer_class = CONDICAO_CAMADASerializer

class CANAL_VENDASViewSet(viewsets.ModelViewSet):
    queryset = CANAL_VENDAS.objects.all()
    serializer_class = CANAL_VENDASSerializer

class LINHA_NEGOCIOViewSet(viewsets.ModelViewSet):
    queryset = LINHA_NEGOCIO.objects.all()
    serializer_class = LINHA_NEGOCIOSerializer

class ESQUEMA_DE_CALCULOViewSet(viewsets.ModelViewSet):
    queryset = ESQUEMA_DE_CALCULO.objects.all()
    serializer_class = ESQUEMA_DE_CALCULOSerializer

class CAMADA_ESQUEMAViewSet(viewsets.ModelViewSet):
    queryset = CAMADA_ESQUEMA.objects.all()
    serializer_class = CAMADA_ESQUEMASerializer

class PRECOViewSet(viewsets.ModelViewSet):
    queryset = PRECO.objects.all()
    serializer_class = PRECOSerializer
        