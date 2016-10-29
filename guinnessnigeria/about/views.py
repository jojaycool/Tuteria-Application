'''
Created on 27 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404

from guinnessnigeria.about import models


class BoardOfDirectorsList(generic_views.ListView):

    def get_queryset(self):
        return models.BoardMember.permitted.all()


class BoardOfDirectorsDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.BoardMember, slug=self.kwargs['slug'])


class ExecutiveList(generic_views.ListView):

    def get_queryset(self):
        return models.Executive.permitted.all()


class ExecutiveDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.Executive, slug=self.kwargs['slug'])
