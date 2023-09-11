from django import forms
from .models import Confirmacao

class ConfirmacaoForm(forms.ModelForm):
    class Meta:
        model = Confirmacao
        fields = ['id', 'name', 'email', 'phone', 'attend', 'people_count', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Confirmacao.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já foi registrado.")
        return email