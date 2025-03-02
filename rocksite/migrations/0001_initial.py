# Generated by Django 4.2 on 2023-05-02 12:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontoDeAmostragem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero_pa', models.CharField(max_length=50, null=True)),
                ('data_coleta', models.DateField(null=True)),
                ('tipo', models.CharField(max_length=100)),
                ('situacao_coleta', models.CharField(max_length=100, null=True)),
                ('material_origem', models.CharField(max_length=100, null=True)),
                ('localizacao_id', models.UUIDField()),
            ],
        ),
    ]
