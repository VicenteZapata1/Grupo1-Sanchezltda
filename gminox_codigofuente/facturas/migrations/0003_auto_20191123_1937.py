# Generated by Django 2.2.7 on 2019-11-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_auto_20191123_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompragminox',
            name='Iva',
            field=models.IntegerField(blank=(None, 0)),
        ),
    ]
