# Generated by Django 3.2.3 on 2021-05-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_price', models.CharField(max_length=4)),
                ('package_duration', models.CharField(max_length=20)),
            ],
        ),
    ]
