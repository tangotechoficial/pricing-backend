import csv
from datetime import datetime
import io

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import DadosMestre, DadosMestreCSV, DiretrizesEstrategica, DiretrizesEstrategicaCSV
from .serializers import (DadosMestreSerializer, DadosMestreCSVSerializer,
                          DiretrizesEstrategicaSerializer, DiretrizesEstrategicaCSVSerializer)
from .utils import parse_csv_model

class DadosMestreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = DadosMestre.objects.all()
    serializer_class = DadosMestreSerializer


class DadosMestreCSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DadosMestre to be viewed or edited.
    """
    queryset = DadosMestreCSV.objects.all()
    serializer_class = DadosMestreCSVSerializer

    def create(self, request):
        DadosMestre.objects.all().delete()
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        dadosmestres = parse_csv_model(csvfile, DadosMestre)
        for dadosmestre in dadosmestres:
            dadosmestre.save()
        
        return Response({'status': 'CSV Imported Successfully'})

class DiretrizesEstrategicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = DiretrizesEstrategica.objects.all()
    serializer_class = DiretrizesEstrategicaSerializer


class DiretrizesEstrategicaCSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DiretrizesEstrategica to be viewed or edited.
    """
    queryset = DiretrizesEstrategica.objects.all()
    serializer_class = DiretrizesEstrategicaCSVSerializer

    def create(self, request):
        DadosMestre.objects.all().delete()
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        diretrizesestrategicas = parse_csv_model(csvfile, DiretrizesEstrategica)
        for diretrizesestrategica in diretrizesestrategicas:
            diretrizesestrategica.DATINI = datetime.strptime(diretrizesestrategica.DATINI, "%d%b%Y:%H:%M:%S")
            diretrizesestrategica.save()
        return Response({'status': 'CSV Imported Successfully'})
