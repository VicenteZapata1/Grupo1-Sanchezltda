# Generated by Django 2.0.2 on 2019-11-14 04:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_cliente'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cliente',
            managers=[
                ('clientes', django.db.models.manager.Manager()),
            ],
        ),
    ]
