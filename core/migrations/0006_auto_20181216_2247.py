# Generated by Django 2.1.4 on 2018-12-17 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_tipodespesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoDespesa'),
        ),
    ]
