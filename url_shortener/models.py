# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from services import generer


class ShortURL(models.Model):
    
    # Attributes
    #--------------------------------------------------
    
    url = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=20, blank=True, null=True)
    nb_acces = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")


    # Methods
    #--------------------------------------------------
    
    def __unicode__(self):
        return "[{0}] {1}".format(self.code, self.url)
    
    def save(self, *args, **kwargs):
        if self.pk is None: # Si l'entité n'existe pas encore en base
            self.code = generer(6)
        super(ShortURL, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"

