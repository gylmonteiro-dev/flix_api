# Generated by Django 5.1.1 on 2024-11-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atores', '0001_initial'),
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='atores',
            field=models.ManyToManyField(blank=True, null=True, related_name='filmes', to='atores.ator'),
        ),
    ]
