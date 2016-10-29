'''
Created on 22 Mar 2013

@author: michael
'''
from django.views import generic as generic_views

from guinnessnigeria.careers import models


class VacancyList(generic_views.ListView):

    def get_queryset(self):
        return models.Vacancy.objects.all()
