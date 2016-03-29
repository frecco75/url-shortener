# -*- coding: utf-8 -*-
from django import forms
from url_shortener.models import ShortURL

class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ('url', 'pseudo')    