from django import forms
from socket import fromshare
from .models import Person, Madeira


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_madeira'].queryset = Madeira.objects.none()

        if 'cod_nome_popular' in self.data:
            print("ENtrei no IF aqui")

            try:
                #country_id = int(self.data.get('country'))
                nome_popID = int(self.data.get('cod_nome_popular'))
                print(nome_popID)
                self.fields['cod_madeira'].queryset = Madeira.objects.filter(id_cod_nome_popular=nome_popID).order_by('nome_popular')
            except (ValueError, TypeError):
               pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['cod_madeira'].queryset = self.instance.nome_popular.madeira_set.order_by('nome_popular')
