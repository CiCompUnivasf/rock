# Generated by Django 4.2 on 2023-05-04 12:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rocksite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=500)),
                ('uf', models.CharField(max_length=2)),
                ('municipio', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='pontodeamostragem',
            name='localizacao_id',
        ),
        migrations.CreateModel(
            name='Horizonte',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profundidade_superior', models.IntegerField()),
                ('profundidade_inferior', models.IntegerField()),
                ('h2o', models.FloatField(null=True)),
                ('kci', models.FloatField(null=True)),
                ('calcio', models.FloatField(null=True)),
                ('simbolo', models.CharField(max_length=3)),
                ('ponto_de_amostragem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rocksite.pontodeamostragem')),
            ],
        ),
        migrations.AddField(
            model_name='pontodeamostragem',
            name='localizacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rocksite.localizacao'),
            preserve_default=False,
        ),
    ]
