'''
Created on 22 Mar 2013

@author: michael
'''
from django.contrib import admin

from guinnessnigeria.news_and_media import models

admin.site.register(models.PressRelease)
admin.site.register(models.Publication)
