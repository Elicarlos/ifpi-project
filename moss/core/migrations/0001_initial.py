# Generated by Django 2.0.6 on 2018-07-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=17)),
                ('nome', models.CharField(max_length=50)),
                ('defeito', models.CharField(max_length=200)),
                ('nome_sistema', models.CharField(max_length=50)),
                ('data_abertura', models.DateTimeField(verbose_name='Data de Abertura de Chamdado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=17)),
                ('razao_social', models.CharField(max_length=50)),
                ('fantasia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
