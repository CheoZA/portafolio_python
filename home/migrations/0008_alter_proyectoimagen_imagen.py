# Generated by Django 3.2.9 on 2021-11-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_proyectoimagen_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectoimagen',
            name='imagen',
            field=models.ImageField(upload_to='static/upload/images/'),
        ),
    ]