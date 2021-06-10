# Generated by Django 2.2 on 2021-06-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoaplication', '0002_local_locatario_orden_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('IdCliente', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Contraceña', models.CharField(max_length=30)),
                ('Direccion', models.CharField(blank=True, max_length=50)),
                ('Status', models.IntegerField(help_text='Puede tomar el valor de Activo = 1 o Inactivo = 0')),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('IdPago', models.IntegerField(primary_key=True, serialize=False)),
                ('ComisionPorcentaje', models.FloatField()),
                ('ComisionPesos', models.FloatField(help_text='De acuerdo al porcetaje de comision, se agregan los pesos')),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
    ]
