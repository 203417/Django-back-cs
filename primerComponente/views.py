from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Importacion de modelos agregados
from primerComponente.models import PrimerTabla

# Importacion de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.
class PrimerTablaList(APIView):
    def get(self, request, format = None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset, many = True, context = {'request': request})
        return Response(serializer.data)