# Generated by Django 2.2.5 on 2019-09-11 02:20

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('cantidad', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('ancho', models.IntegerField()),
                ('espesor', models.IntegerField()),
            ],
            managers=[
                ('materiales', django.db.models.manager.Manager()),
            ],
        ),
    ]
