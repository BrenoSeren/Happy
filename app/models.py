from django.db import models


class Estado(models.Model):
    name = models.CharField(max_length=45)

class Cidade (models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=45) 

class Institution(models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    Cidade_id_cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=11)
    atvidade = models.CharField(max_length=45)
    descricao = models.TextField()
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    situacao = models.CharField(max_length=1)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField()

class User(models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    Cidade_id_cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=11)
    situacao = models.CharField(max_length=1)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField()
