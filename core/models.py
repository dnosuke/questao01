from django.db import models
from django.utils import timezone


class Despesa(models.Model):
    tipoDespesa_CHOICES = (
        ('ALIMENTACAO', 'Alimentação'),
        ('ROUPA', 'Roupas'),
        ('REMEDIO', 'Remédio'),
        ('TRANSPORTE', 'Transporte'),
        ('EDUCACAO', 'Educação'),
        ('OUTROS', 'Outros'),
    )

    FormaPagamento_CHOICES = (
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO DE CREDITO', 'Cartão de Crédito'),
        ('CARTAO DE DEBITO', 'Cartão de Débito'),
        ('CARTAO CREDIARIO', 'Cartão Crediário'),
        ('CHEQUE', 'Cheque'),
    )

    data_criacao = models.DateTimeField('data de criação',default=timezone.now)
    tipo_despesa = models.CharField(max_length=100, choices=tipoDespesa_CHOICES)
    descricao = models.CharField('descrição', max_length=200)
    forma_pagamento = models.CharField(max_length=100, choices=FormaPagamento_CHOICES)
    vencimento = models.DateTimeField(blank=True, null=True)
    quitado = models.BooleanField()


    class Meta:
        verbose_name_plural= 'Despesas agendadas'
        verbose_name= 'Despesa agendada'

    def __str__(self):
        return '{}{}-{}'.format(
            self.data.strftime('%d/%m/%Y'),
            self.hora.strftime('%H:%M'),
            self.titulo
        )

    def publish(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.tipo_despesa



