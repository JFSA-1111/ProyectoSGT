# Generated by Django 2.2.2 on 2020-03-02 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_auto_20200228_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='id_usuario',
        ),
    ]