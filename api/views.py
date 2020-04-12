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
from data_scripts.plano_compras_planejado import run_planejado_tela
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
        return planejado in plano de compras using data scripts
        """
        week = request.data.get('week')
        plan_month = request.data.get('plan_month')
        plan_year = request.data.get('plan_year')
        prd = request.data.get('prd')
        est = request.data.get('est')
        cmvcmp = request.data.get('cmvcmp')
        vrbpln = request.data.get('vrbpln')
        planejado = run_planejado_tela(week, plan_month, plan_year, prd, est, cmvcmp, vrbpln, filepd=1, filfat=1)

        return Response(planejado)

class SugeridoViewSet(viewsets.ViewSet):
    """
    API endpoint that adds plano de compras sugerido
    """
    serializer_class = serializers.SugeridoSerializer
    def create(self, request):
        estados = request.data.get('estados', ['MG', 'SC', 'PA'])
        run_sugerido(plan_month=2, plan_year=2020, filepd=1, filfat=1, estados=estados)
        return Response({'status': 'Sugerido calculado com sucesso'})
