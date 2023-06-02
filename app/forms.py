from django import forms
from app.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        field = '__all__'