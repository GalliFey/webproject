# Generated by Django 3.1.4 on 2020-12-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='poster',
            field=models.ImageField(upload_to='posters/', verbose_name='Постер'),
        ),
    ]
