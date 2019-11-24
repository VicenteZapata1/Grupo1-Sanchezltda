# Generated by Django 2.2.5 on 2019-11-20 03:16

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_auto_20191115_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('telefono_proveedor', models.CharField(max_length=12)),
                ('rut', models.CharField(max_length=11)),
                ('email_proveedor', models.CharField(max_length=60)),
                ('representante', models.CharField(max_length=60)),
                ('vendedor', models.CharField(max_length=60)),
                ('telefono_representante', models.CharField(max_length=12)),
                ('email_representante', models.CharField(max_length=60)),
                ('telefono_vendedor', models.CharField(max_length=12)),
                ('email_vendedor', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('giro', models.CharField(max_length=60)),
            ],
            managers=[
                ('proveedores', django.db.models.manager.Manager()),
            ],
        ),
    ]