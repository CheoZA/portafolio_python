# Generated by Django 3.2.9 on 2021-11-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211128_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectoimagen',
            name='titulo',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
