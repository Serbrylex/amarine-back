# Generated by Django 4.2.1 on 2023-06-01 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_name', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
            ],
        ),
    ]