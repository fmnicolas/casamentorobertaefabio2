from django import forms
from .models import Confirmacao
from django.core.exceptions import ValidationError

class ConfirmacaoForm(forms.ModelForm):
    class Meta:
        model = Confirmacao
        fields = ['name', 'email', 'phone', 'attend', 'people_count', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Confirmacao.objects.filter(email=email).exists():
            raise ValidationError("Este email já foi registrado.")
        return email