from django import forms
from django.forms import ModelForm
from .models import MensagemDeContato


class ContatoForm(ModelForm):
    class Meta:
        model = MensagemDeContato
        fields = '__all__'