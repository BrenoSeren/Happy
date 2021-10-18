from django.forms import ModelForm
from app.models import Doacao, Institution, User

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

class DoacaoForm(ModelForm):
    class Meta:
        model = Doacao
        fields = [
            'valor'
        ]

class DoacaoCompForm(ModelForm):
    class Meta:
        model = Doacao
        fields = [
            'Instituicoes', 'User',
            'valor'
        ]