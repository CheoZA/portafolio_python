# Generated by Django 3.2.9 on 2021-11-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_persona_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
    ]
