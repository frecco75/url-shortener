# -*- coding: utf-8 -*-
from django.contrib import admin
from url_shortener.models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    # Ordre d'affichage pour la consultation
    list_display   = ('url', 'code', 'pseudo', 'nb_acces', 'date') 
    list_filter    = ('pseudo','nb_acces',)
    date_hierarchy = 'date'
    ordering       = ('-nb_acces', 'date', 'url', 'pseudo')
    search_fields  = ('pseudo',)
    
    # Ordre d'affichage pour l'édition d'un tuple
    fields = ('url', 'code', 'pseudo') 
    
admin.site.register(ShortURL, ShortURLAdmin)