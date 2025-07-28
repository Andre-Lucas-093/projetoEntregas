from django import forms
from .models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = [ 'vendedor', 'veiculo', 'endereco','horario']
        widgets = {
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }