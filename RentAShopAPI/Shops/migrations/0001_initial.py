# Generated by Django 4.0.4 on 2022-04-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop_images')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
                ('area', models.BigIntegerField()),
                ('deposit', models.BigIntegerField()),
                ('rent', models.BigIntegerField()),
                ('address', models.TextField()),
                ('latitude', models.BigIntegerField()),
                ('longitude', models.BigIntegerField()),
                ('images', models.ManyToManyField(to='Shops.shopimage')),
            ],
        ),
    ]
