# Generated by Django 3.2.9 on 2021-11-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(),
        ),
    ]
