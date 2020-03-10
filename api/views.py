import csv
from datetime import datetime
import io

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
from .utils import parse_csv_model

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
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = models.PlanoCompras.objects.all()
    serializer_class = serializers.PlanoComprasSerializer
