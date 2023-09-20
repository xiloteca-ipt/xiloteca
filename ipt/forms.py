from django import forms
from ipt.models import Busca, Consulta


class BuscaForm(forms.ModelForm):
    class Meta:
        model = Busca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
