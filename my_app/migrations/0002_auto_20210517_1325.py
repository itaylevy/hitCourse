# Generated by Django 3.2.3 on 2021-05-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_price',
            field=models.CharField(max_length=4),
        ),
    ]
