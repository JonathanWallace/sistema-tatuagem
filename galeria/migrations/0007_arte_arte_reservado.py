# Generated by Django 5.0.4 on 2024-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_arte_arte_lugar_corpo_alter_arte_arte_qntd_sessoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='arte_reservado',
            field=models.BooleanField(default=False),
        ),
    ]
