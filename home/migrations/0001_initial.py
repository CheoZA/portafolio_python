# Generated by Django 3.2.9 on 2021-11-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.TimeField()),
            ],
        ),
    ]