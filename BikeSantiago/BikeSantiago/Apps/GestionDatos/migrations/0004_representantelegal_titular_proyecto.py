# Generated by Django 4.0.4 on 2023-02-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDatos', '0003_alter_station_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='representanteLegal',
            fields=[
                ('id_titular', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
                ('domicilio', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='titular',
            fields=[
                ('id_titular', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
                ('domicilio', models.CharField(max_length=500)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
                ('tipo_proyecto', models.CharField(max_length=100)),
                ('monto_inversion', models.CharField(max_length=100)),
                ('estado_actual', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('descripcion_proyecto', models.CharField(max_length=2000)),
                ('representante_legal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionDatos.representantelegal')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionDatos.titular')),
            ],
        ),
    ]
