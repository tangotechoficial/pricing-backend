import csv
from datetime import datetime
import io

from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response

from . import models
from . import serializers
from pricing_parsing.models import Movplncmpcal
from .utils import parse_csv_model
from data_scripts.plano_compras_planejado import run_planejado
from data_scripts.plano_compras_sugerido import run_sugerido

class FornecedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Fornecedor to be viewed or edited.
    """
    queryset = models.Fornecedor.objects.all()
    serializer_class = serializers.FornecedorSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comprador to be viewed or edited.
    """
    queryset = models.Comprador.objects.all()
    serializer_class = serializers.CompradorSerializer

class TabAuxGrpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TabAuxGrp to be viewed or edited.
    """
    queryset = models.TabAuxGrp.objects.all()
    serializer_class = serializers.TabAuxGrpSerializer

class RelacionamentoFilialRegiaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RelacionamentoFilialRegiao to be viewed or edited.
    """
    queryset = models.RelacionamentoFilialRegiao.objects.all()
    serializer_class = serializers.RelacionamentoFilialRegiaoSerializer

class MercadoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mercadoria to be viewed or edited.
    """
    queryset = models.Mercadoria.objects.all()
    serializer_class = serializers.MercadoriaSerializer

class RepresentanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Representante to be viewed or edited.
    """
    queryset = models.Representante.objects.all()
    serializer_class = serializers.RepresentanteSerializer

class VendasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Vendas to be viewed or edited.
    """
    queryset = models.Vendas.objects.all()
    serializer_class = serializers.VendasSerializer

class VerbaeBCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows VerbaeBC to be viewed or edited.
    """
    queryset = models.VerbaeBC.objects.all()
    serializer_class = serializers.VerbaeBCSerializer

class ElasticidadeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Elasticidade to be viewed or edited.
    """
    queryset = models.Elasticidade.objects.all()
    serializer_class = serializers.ElasticidadeSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Estoque to be viewed or edited.
    """
    queryset = models.Estoque.objects.all()
    serializer_class = serializers.EstoqueSerializer

class CompetitividadeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Competitividade to be viewed or edited.
    """
    queryset = models.Competitividade.objects.all()
    serializer_class = serializers.CompetitividadeSerializer

class DadosMestre_VerbaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = models.DadosMestre_Verba.objects.all()
    serializer_class = serializers.DadosMestre_VerbaSerializer


class DadosMestre_VerbaCSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = models.DadosMestre_VerbaCSV.objects.all()
    serializer_class = serializers.DadosMestre_VerbaCSVSerializer

    def create(self, request):
        models.DadosMestre_Verba.objects.all().delete()
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        dadosmestres = parse_csv_model(csvfile, models.DadosMestre_Verba)
        for dadosmestre in dadosmestres:
            dadosmestre.save()
        
        return Response({'status': 'CSV Imported Successfully'})


class DadosMestre_ComposicaoPrecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = models.DadosMestre_ComposicaoPreco.objects.all()
    serializer_class = serializers.DadosMestre_ComposicaoPrecoSerializer


class DadosMestre_ComposicaoPrecoCSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = models.DadosMestre_ComposicaoPrecoCSV.objects.all()
    serializer_class = serializers.DadosMestre_ComposicaoPrecoCSVSerializer

    def create(self, request):
        models.DadosMestre_ComposicaoPreco.objects.all().delete()
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        dadosmestres = parse_csv_model(csvfile, models.DadosMestre_ComposicaoPreco)
        for dadosmestre in dadosmestres:
            dadosmestre.DATA_PRECO = datetime.strptime(dadosmestre.DATA_PRECO, "%m/%d/%Y %H:%M")
            print (vars(dadosmestre))
            dadosmestre.save()
        
        return Response({'status': 'CSV Imported Successfully'})

class DiretrizesEstrategicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.all()
    serializer_class = serializers.DiretrizesEstrategicaSerializer


class DiretrizesEstrategicaCSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.DiretrizesEstrategica.objects.all()
    serializer_class = serializers.DiretrizesEstrategicaCSVSerializer

    def create(self, request):
        models.DiretrizesEstrategica.objects.all().delete()
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        diretrizesestrategicas = parse_csv_model(csvfile, models.DiretrizesEstrategica)
        for diretrizesestrategica in diretrizesestrategicas:
            diretrizesestrategica.DATINI = datetime.strptime(diretrizesestrategica.DATINI, "%d%b%Y:%H:%M:%S")
            diretrizesestrategica.save()
        return Response({'status': 'CSV Imported Successfully'})

class PlanoComprasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlanoCompras to be viewed or edited.
    """
    queryset = models.PlanoCompras.objects.all()
    serializer_class = serializers.PlanoComprasSerializer

class OtimizadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Otimizador to be viewed or edited.
    """
    queryset = models.Otimizador.objects.all()
    serializer_class = serializers.OtimizadorSerializer

class PlanejadoViewSet(viewsets.ViewSet):
    """
    API endpoint that adds plano de compras planejado
    """
    serializer_class = serializers.PlanejadoSerializer
    def create(self, request):
        """
        Insert register in plano de compras using data scripts
        """
        CODPRD = request.data.get('CODPRD')
        CODESTUNI = request.data.get('CODESTUNI')
        user_input = {
            'VERBA_WEEK1': request.data.get('VERBA_WEEK1'),
            'VERBA_WEEK2': request.data.get('VERBA_WEEK2'),
            'VERBA_WEEK3': request.data.get('VERBA_WEEK3'),
            'VERBA_WEEK4': request.data.get('VERBA_WEEK4'),
            'VERBA_WEEK5': request.data.get('VERBA_WEEK5'),
            'CMVCMP_WEEK1': request.data.get('CMVCMP_WEEK1'),
            'CMVCMP_WEEK2': request.data.get('CMVCMP_WEEK2'),
            'CMVCMP_WEEK3': request.data.get('CMVCMP_WEEK3'),
            'CMVCMP_WEEK4': request.data.get('CMVCMP_WEEK4'),
            'CMVCMP_WEEK5': request.data.get('CMVCMP_WEEK5')
        }
        planejado = run_planejado(CODPRD, CODESTUNI, plan_month=2, plan_year=2020, user_input=user_input, filepd=1, filfat=1)
        planejado = planejado.to_dict()
        for week in range(0, 5):
            movplncmpcal = Movplncmpcal()
            movplncmpcal.codprd = planejado['CODPRD'][week]
            movplncmpcal.codfilepd = planejado['CODFILEPD'][week]
            movplncmpcal.codfilfat = planejado['CODFILFAT'][week]
            movplncmpcal.codestuni = planejado['CODESTUNI'][week]
            movplncmpcal.month = planejado['MONTH'][week]
            movplncmpcal.year = planejado['YEAR'][week]
            movplncmpcal.week = planejado['WEEK'][week]
            movplncmpcal.volvndsug = planejado['VOLVNDSUG'][week]
            movplncmpcal.volvndsugalc = planejado['VOLVNDSUGALC'][week]
            movplncmpcal.mrgbrtperocd = planejado['MRGBRTPEROCD'][week]
            movplncmpcal.vlrpcosug = planejado['VLRPCOSUG'][week]
            movplncmpcal.mrgbrtperocd = planejado['MRGBRTPEROCD'][week]
            movplncmpcal.vlrpcobasesug = planejado['VLRPCOBASESUG'][week]
            movplncmpcal.vlrimptotsug = planejado['VLRIMPTOTSUG'][week]
            movplncmpcal.vlricmssug = planejado['VLRICMSSUG'][week]
            movplncmpcal.vlrpiscofsug = planejado['VLRPISCOFSUG'][week]
            movplncmpcal.vlrdevsug = planejado['VLRDEVSUG'][week]
            movplncmpcal.vlrflxsug = planejado['VLRFLXSUG'][week]
            movplncmpcal.vlrmrgbrtsug = planejado['VLRMRGBRTSUG'][week]
            movplncmpcal.vrbuntsugsug = planejado['VRBUNTSUGSUG'][week]
            movplncmpcal.vlrvrbplan = planejado['VLRVRBPLAN'][week]
            movplncmpcal.vlrcmvpcosug = planejado['VLRCMVPCOSUG'][week]
            movplncmpcal.vlrcmvpcoatu = planejado['VLRCMVPCOATU'][week]
            movplncmpcal.vlrcmvcmpatu = planejado['VLRCMVCMPATU'][week]
            movplncmpcal.vlrpcomrc = planejado['VLRPCOMRC'][week]
            movplncmpcal.vlrcompsug = planejado['VLRCOMPSUG'][week]
            movplncmpcal.volvndpln = planejado['VOLVNDPLN'][week]
            movplncmpcal.vlrpcopln = planejado['VLRPCOPLN'][week]
            movplncmpcal.vlrpcobasepln = planejado['VLRPCOBASEPLN'][week]
            movplncmpcal.vlrimptotpln = planejado['VLRIMPTOTPLN'][week]
            movplncmpcal.vlricmspln = planejado['VLRICMSPLN'][week]
            movplncmpcal.vlrpiscofpln = planejado['VLRPISCOFPLN'][week]
            movplncmpcal.vlrdevpln = planejado['VLRDEVPLN'][week]
            movplncmpcal.vlrflxpln = planejado['VLRFLXPLN'][week]
            movplncmpcal.vlrmrgbrtpln = planejado['VLRMRGBRTPLN'][week]
            movplncmpcal.vrbuntsugpln = planejado['VRBUNTSUGPLN'][week]
            movplncmpcal.vlrvrbpln = planejado['VLRVRBPLN'][week]
            movplncmpcal.vlrcmvpcopln = planejado['VLRCMVPCOPLN'][week]
            movplncmpcal.vlrcmvcmppln = planejado['VLRCMVCMPPLN'][week]
            movplncmpcal.vlrcomppln = planejado['VLRCOMPPLN'][week]

            movplncmpcal.save()

        return Response({'status': 'Planejado calculado com sucesso'})

class SugeridoViewSet(viewsets.ViewSet):
    """
    API endpoint that adds plano de compras sugerido
    """
    serializer_class = serializers.SugeridoSerializer
    def create(self, request):
        estados = request.data.get('estados', ['MG', 'SC', 'PA'])
        run_sugerido(plan_month=2, plan_year=2020, filepd=1, filfat=1, estados=estados)
        return Response({'status': 'Sugerido calculado com sucesso'})
