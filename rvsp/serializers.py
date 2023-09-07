from rest_framework import serializers
from .models import Confirmacao

class ConfirmacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Confirmacao
        fields = ['id', 'name', 'email', 'phone', 'attend', 'people_count', 'message']