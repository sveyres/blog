# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length=20, verbose_name='Label')

    def __unicode__(self):
        return "Catégorie : %s" % self.label

        class Meta:
            verbose_name = 'Catégorie'

class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='Titre')
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(verbose_name='Contenu')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{0} | {1}'.format(self.creation_date, self.title)

    class Meta:
        verbose_name = 'Article'
