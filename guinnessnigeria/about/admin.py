'''
Created on 22 Mar 2013

@author: michael
'''
from django.contrib import admin

from guinnessnigeria.about import models

admin.site.register(models.BoardMember)
admin.site.register(models.Executive)
