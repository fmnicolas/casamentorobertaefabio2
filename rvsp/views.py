from django.shortcuts import render
from rest_framework import viewsets
from .models import Confirmacao
from .serializers import ConfirmacaoSerializer

def index(request):

    return render(request, 'rvsp/index.html')

class ConfirmacaoViewSet(viewsets.ModelViewSet):
    queryset = Confirmacao.objects.all()
    serializer_class = ConfirmacaoSerializer