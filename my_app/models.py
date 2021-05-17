from django.db import models


class Package(models.Model):
    package_name = models.CharField(max_length=100)
    package_price = models.CharField(max_length=4)
    package_duration = models.CharField(max_length=20)

