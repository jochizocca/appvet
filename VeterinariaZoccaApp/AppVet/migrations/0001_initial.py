# Generated by Django 4.0.3 on 2022-04-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido')),
                ('dni', models.IntegerField(verbose_name='dni')),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('raza', models.CharField(max_length=20, verbose_name='raza')),
            ],
        ),
        migrations.CreateModel(
            name='turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
