# Generated by Django 3.2.8 on 2021-10-18 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211018_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='Cidade_id_cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='Estado_id_estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.estado'),
        ),
    ]
