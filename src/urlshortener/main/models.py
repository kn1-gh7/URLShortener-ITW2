from django.db import models

class ShortURLS(models.Model):
    short_url = models.CharField(max_length=8, unique=True)
    long_url = models.URLField("URL", unique=True)
