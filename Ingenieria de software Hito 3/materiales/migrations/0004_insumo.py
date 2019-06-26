# Generated by Django 2.2.2 on 2019-06-23 22:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0003_auto_20190623_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
                ('cantidad', models.IntegerField()),
            ],
            managers=[
                ('insumos', django.db.models.manager.Manager()),
            ],
        ),
    ]
