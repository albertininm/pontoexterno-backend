# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)
    CEP = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

# Obs: Talvez seja melhor usar o user padrao do django
class Usuario(models.Model):
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class StatusTarefa(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Tarefa(models.Model):
    statusTarefa = models.ForeignKey(StatusTarefa)

    descricao = models.CharField(max_length=255)
    observacao = models.CharField(max_length=255)
    horarioRequisitado = models.DateTimeField()
    horarioInicial = models.DateTimeField()
    HorarioFinal = models.DateTimeField()

    def __str__(self):
        return "Status:"+str(self.statusTarefa)+"\nObs: "+str(self.observacao)


class Ponto(models.Model):
    idUsuario = models.ForeignKey(Usuario)

    dataHoraChegada = models.DateTimeField()
    dataHoraSaida = models.DateTimeField()
    justificativaChegada = models.CharField(max_length=255)
    justificativaSaida = models.CharField(max_length=255)
    localizacaoChegada = models.CharField(max_length=255)
    localizacaoSaida = models.CharField(max_length=255)

    def __str__(self):
        return "Usuario:"+str(self.idUsuario)

class CompensacaoHora(models.Model):
    idFuncionario = models.ForeignKey(Usuario, related_name="id_funcionario", on_delete=models.CASCADE)
    idAdmin = models.ForeignKey(Usuario, related_name="id_admin")
    data = models.DateField()
    quantidadeHoras = models.IntegerField()
    justificativa = models.CharField(max_length=255)

    def __str__(self):
        return "Funcionario:"+str(self.idFuncionario)+"\Admin: "+str(self.idAdmin)