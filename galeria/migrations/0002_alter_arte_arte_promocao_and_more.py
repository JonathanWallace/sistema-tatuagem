# Generated by Django 5.0.4 on 2024-05-04 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='arte_promocao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promo_arte', to='galeria.promocao'),
        ),
        migrations.AlterField(
            model_name='arte',
            name='arte_qntd_sessoes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tatuagem',
            name='tatuagem_duracao_servico',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
