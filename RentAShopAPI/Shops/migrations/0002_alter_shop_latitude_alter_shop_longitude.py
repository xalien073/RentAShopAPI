# Generated by Django 4.0.4 on 2022-04-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
