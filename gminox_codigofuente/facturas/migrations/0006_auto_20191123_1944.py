# Generated by Django 2.2.7 on 2019-11-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0005_auto_20191123_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompragminox',
            name='Iva',
            field=models.IntegerField(blank=(None, 0), null=True),
        ),
        migrations.AlterField(
            model_name='facturacompragminox',
            name='Monto',
            field=models.IntegerField(blank=(None, 0), null=True),
        ),
        migrations.AlterField(
            model_name='facturacompragminox',
            name='NumeroFactura',
            field=models.PositiveIntegerField(blank=(None, 0), null=True),
        ),
        migrations.AlterField(
            model_name='facturacompragminox',
            name='Total',
            field=models.IntegerField(blank=(None, 0), null=True),
        ),
    ]