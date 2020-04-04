from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SEQ_CAMPO, SEQUENCIA, SEQ_AUX, CHAVE_CONTAS, TIPOVALOR, CAMADA, CONDICAO, CONDICAO_SEQUENCIA, ESQUEMA_DE_CALCULO, PRECO, CONDICAO_CAMADA_ESQUEMA, MERCADORIA, FILIAL, FATURAMENTO, ESTADO, REGION
from .serializer import SEQ_CAMPOSerializer, SEQUENCIASerializer, SEQ_AUXSerializer, CHAVE_CONTASSerializer, TIPOVALORSerializer, CAMADASerializer, CONDICAOSerializer, CONDICAO_SEQUENCIASerializer, ESQUEMA_DE_CALCULOSerializer, PRECOSerializer, CONDICAO_CAMADA_ESQUEMASerializer, MERCADORIASerializer, FILIALSerializer, FATURAMENTOSerializer, ESTADOSerializer, REGIONSerializer, CONDICAOSEQSerializer, SEQUENCIACAMPOSerializer, CAMADACONDSerializer


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

class SEQUENCIACAMPOViewSet(viewsets.ModelViewSet):
    queryset = SEQUENCIA.objects.all()
    serializer_class = SEQUENCIACAMPOSerializer

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
