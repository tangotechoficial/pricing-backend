import csv
import io

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import DadosMestre, DadosMestreCSV
from .serializers import DadosMestreSerializer, DadosMestreCSVSerializer


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
        csvfile = request.data.get('csvfile').read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(csvfile))
        for row in reader:
            dadosmestre = DadosMestre()
            for field in row.keys():
                setattr(dadosmestre, field.lower(), row[field])

            dadosmestre.save()
        return Response({'status': 'CSV Imported Successfully'})
