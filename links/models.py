from django.db import models

class Link(models.Model):
    long_url = models.URLField(verbose_name='URL', unique=True)
    date_add = models.DateField(auto_now_add=True)
