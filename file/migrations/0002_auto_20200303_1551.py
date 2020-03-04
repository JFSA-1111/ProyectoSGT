# Generated by Django 2.2.2 on 2020-03-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200303_1551'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=35)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grabacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=45)),
                ('url', models.FileField(upload_to='audio/mp3')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='llamadasentrantes',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='RegistroLlamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre_contesta', models.CharField(max_length=45, null=True)),
                ('fecha_entrega', models.DateField(null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('realizado', models.BooleanField(default=False, null=True)),
                ('id_estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='file.Estado')),
                ('id_grabacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='file.Grabacion')),
                ('id_llamada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='file.LlamadasEntrantes')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Perfil')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='llamadasentrantes',
            name='id_archivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='file.Archivo'),
            preserve_default=False,
        ),
    ]