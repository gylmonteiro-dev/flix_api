# Generated by Django 5.1.1 on 2024-10-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('nacionalidade', models.CharField(choices=[('BR', 'Brasil'), ('US', 'Estados Unidos'), ('FR', 'França'), ('DE', 'Alemanha'), ('ES', 'Espanha'), ('CA', 'Canadá'), ('AU', 'Austrália'), ('IN', 'Índia'), ('CN', 'China'), ('JP', 'Japão'), ('RU', 'Rússia'), ('GB', 'Reino Unido'), ('IT', 'Itália'), ('AR', 'Argentina'), ('MX', 'México'), ('PT', 'Portugal'), ('NL', 'Países Baixos'), ('CH', 'Suíça'), ('KR', 'Coreia do Sul'), ('SA', 'Arábia Saudita'), ('EG', 'Egito'), ('NZ', 'Nova Zelândia'), ('TR', 'Turquia'), ('AE', 'Emirados Árabes Unidos')], max_length=3)),
            ],
        ),
    ]