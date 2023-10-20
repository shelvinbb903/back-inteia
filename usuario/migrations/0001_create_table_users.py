# Generated by Django 3.2.6 on 2023-10-19 20:25

from django.db import migrations, models
import django.db.models.deletion
from usuario.models.Roles import Roles

def cargar_roles(apps, schema_editor):
    rol = Roles(nombre='Operador logístico')
    rol.save()

    rol = Roles(nombre='Pasajero')
    rol.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=150)),
                ('contrasena', models.CharField(max_length=250)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.roles')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.RunPython(cargar_roles),
    ]