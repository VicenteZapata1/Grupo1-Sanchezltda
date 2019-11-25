# Generated by Django 2.2.7 on 2019-11-24 23:14

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCompraGminox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proveedor', models.CharField(max_length=100)),
                ('NumeroFactura', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Fecha', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Monto', models.IntegerField(blank=True, default=0, null=True)),
                ('Iva', models.IntegerField(blank=True, default=0, null=True)),
                ('Total', models.IntegerField(blank=True, default=0, null=True)),
                ('pdf', models.FileField(upload_to='facturascompra/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
    ]
