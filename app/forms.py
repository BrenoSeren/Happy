from django.forms import ModelForm
from app.models import Institution

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = [
            'name', 'email', 'celular', 'atvidade', 'descricao',
            'cep', 'bairro', 'endereco'
        ]