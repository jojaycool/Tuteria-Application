'''
Created on 22 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.contrib.contenttypes.models import ContentType

from guinnessnigeria.news_and_media import models


class PressReleaseList(generic_views.ListView):

    def get_queryset(self):
        return models.PressRelease.permitted.order_by('-publish_date_time')


class PressReleaseDetail(generic_views.DetailView):

    def get_object(self):
        try:
            return models.PressRelease.permitted.get(pk=self.kwargs['pk'])
        except models.PressRelease.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super(PressReleaseDetail, self).get_context_data(**kwargs)
        context.update({'content_type':
                        ContentType.objects.get_for_model(self.object),
                        'press_releases':
                        models.PressRelease.permitted.all()[:5]})

        return context


class PublicationList(generic_views.ListView):

    age_gate_url = '/age_gate'

    def get_queryset(self):
        return models.Publication.objects.all().order_by('-publication_date')
