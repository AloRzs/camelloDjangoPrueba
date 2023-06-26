# Generated by Django 3.1.1 on 2023-06-26 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=30)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('total', models.IntegerField(max_length=10)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroVenta',
            fields=[
                ('id_regis_venta', models.AutoField(primary_key=True, serialize=False)),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(max_length=4)),
                ('subtotal', models.IntegerField(max_length=8)),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id_combo', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField(max_length=6)),
                ('stock', models.IntegerField(max_length=4)),
                ('foto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('id_detalle_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.detalleventa')),
            ],
        ),
    ]
