# Generated by Django 5.1.1 on 2024-09-10 16:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testeDjangoModels', '0002_alter_departament_id_alter_usuario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 13, 4, 14, 363355), null=True),
        ),
        migrations.AddField(
            model_name='departament',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='departament',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testeDjangoModels.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 13, 4, 14, 363355)),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
