# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='Titre')
    body = models.TextField(verbose_name='Contenu')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')

    def __unicode__(self):
        return '{0} | {1}'.format(self.creation_date.stfrdate('%d/%m/%Y'), self.title)

    def get_slug(self):
        return self.title.replace(" ", "-").lower()

    class Meta:
        verbose_name = 'Article'
