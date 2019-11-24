# Generated by Django 2.0.2 on 2019-11-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0002_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('telefono_cliente', models.CharField(max_length=12)),
                ('rut', models.CharField(max_length=11)),
                ('email_cliente', models.CharField(max_length=60)),
                ('representante', models.CharField(max_length=60)),
                ('telefono_representante', models.CharField(max_length=12)),
                ('email_representante', models.CharField(max_length=60)),
                ('dirección', models.CharField(max_length=60)),
                ('giro', models.CharField(max_length=60)),
            ],
        ),
    ]