# Generated by Django 5.2 on 2025-04-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('finished_at', models.DateField(null=True)),
            ],
        ),
    ]
