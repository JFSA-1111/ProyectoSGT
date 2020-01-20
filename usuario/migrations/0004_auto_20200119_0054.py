# Generated by Django 2.2.2 on 2020-01-19 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_conectado_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conectado',
            name='usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='conexion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Conectado'),
        ),
    ]