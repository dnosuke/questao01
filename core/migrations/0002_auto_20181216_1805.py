# Generated by Django 2.1.4 on 2018-12-16 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criação')),
                ('tipo_despesa', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200, verbose_name='descrição')),
                ('forma_pagamento', models.CharField(max_length=200)),
                ('vencimento', models.DateTimeField(blank=True, null=True)),
                ('quitado', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Despesa agendada',
                'verbose_name_plural': 'Despesas agendadas',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
