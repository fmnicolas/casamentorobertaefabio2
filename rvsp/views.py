from django.http import JsonResponse
from django.shortcuts import render
from .forms import ConfirmacaoForm
from rest_framework import viewsets
from .models import Confirmacao
from .serializers import ConfirmacaoSerializer

def index(request):
    return render(request, 'rvsp/index.html')

def verificar_email(request):
    if request.method == 'POST':
        form = ConfirmacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ConfirmacaoForm()
    
    return render(request, 'index.html', {'form': form})

class ConfirmacaoViewSet(viewsets.ModelViewSet):
    queryset = Confirmacao.objects.all()
    serializer_class = ConfirmacaoSerializer