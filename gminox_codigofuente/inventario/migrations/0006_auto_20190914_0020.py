# Generated by Django 2.2.4 on 2019-09-14 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_despunte'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='herramienta',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='insumo',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='epp',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='epp',
            name='marca',
            field=models.CharField(default='Generico', max_length=20),
        ),
        migrations.AddField(
            model_name='epp',
            name='medida',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='epp',
            name='umedida',
            field=models.CharField(blank=True, default='Talla', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='marca',
            field=models.CharField(default='Generico', max_length=20),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='medida',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='umedida',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='insumo',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='marca',
            field=models.CharField(default='Generico', max_length=20),
        ),
        migrations.AddField(
            model_name='insumo',
            name='umedida',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='medida',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
