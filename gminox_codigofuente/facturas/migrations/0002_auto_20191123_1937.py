# Generated by Django 2.2.7 on 2019-11-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompragminox',
            name='Monto',
            field=models.IntegerField(blank=(None, 0)),
        ),
    ]
