# Generated by Django 4.2.3 on 2023-07-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personagem', models.CharField(max_length=100)),
                ('jogo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
