# Generated by Django 5.2.3 on 2025-07-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tercer_entrega_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banda', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('precio', models.FloatField()),
            ],
        ),
    ]
