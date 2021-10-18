from django.forms import ModelForm
from app.models import Institution, User

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = [
            'name', 'email', 'celular', 'atividade', 'descricao',
            'cep', 'bairro', 'endereco'
            # , 'Cidade_id_cidade', 'Estado_id_estado'
        ]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'email', 'celular',
            # 'Cidade_id_cidade', 'Estado_id_estado'
        ]