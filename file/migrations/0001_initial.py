# Generated by Django 2.2.2 on 2020-01-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LlamadasEntrantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre_solicitante', models.CharField(max_length=50)),
                ('ident_fiscal', models.CharField(max_length=50)),
                ('nombre_destinatario', models.CharField(max_length=50)),
                ('direccion_des_mcia', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('telebox', models.CharField(max_length=50)),
                ('zona_transporte', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('texto_breve_material', models.CharField(max_length=50)),
                ('documento_ventas', models.CharField(max_length=50)),
                ('entrega', models.CharField(max_length=50)),
                ('num_pedido_cliente', models.CharField(max_length=50)),
                ('cantidad_pedido', models.CharField(max_length=50)),
                ('observaciones_inicial', models.CharField(max_length=255)),
                ('denom_articulos', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('barrio', models.CharField(max_length=50)),
                ('ruta', models.CharField(max_length=50)),
                ('hora_inicio', models.CharField(max_length=50)),
                ('hora_final', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
