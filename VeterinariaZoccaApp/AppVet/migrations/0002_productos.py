# Generated by Django 4.0.3 on 2022-04-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_producto', models.CharField(max_length=20, verbose_name='n_producto')),
                ('sku', models.IntegerField()),
            ],
        ),
    ]
