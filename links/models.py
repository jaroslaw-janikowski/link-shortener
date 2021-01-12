from django.db import models

class Link(models.Model):
    short_url = models.CharField(max_length=512, unique=True)
    long_url = models.TextField(verbose_name='URL', unique=True)
    date_add = models.DateField(auto_now_add=True)
