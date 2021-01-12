from django.db import models

class Link(models.Model):
    long_url = models.URLField(verbose_name='URL')  # kontrola dodawania wielu takich samych URL dokonywana jest podczas zapisu
    date_add = models.DateField(auto_now_add=True)
