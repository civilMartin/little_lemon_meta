# Generated by Django 4.2.3 on 2023-07-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=5),
        ),
    ]
