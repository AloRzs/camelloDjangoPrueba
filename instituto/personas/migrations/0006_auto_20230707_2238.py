# Generated by Django 3.1.1 on 2023-07-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_auto_20230707_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]