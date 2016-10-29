from django.db import models
from django.core.urlresolvers import reverse

from unobase.poll import models as poll_models
from unobase import models as unobase_models

from guinnessnigeria.investors import models as investor_models
from guinnessnigeria import monkey

from preferences.models import Preferences


class FrontPageBanner(unobase_models.ContentModel, unobase_models.StateModel):
    url = models.URLField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % self.image

    def get_url(self):
        return self.url or reverse('index')


class SocialMedia(models.Model):
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.facebook_url

    class Meta:
        verbose_name_plural = 'social media'


class SitePreferences(Preferences):
    __module__ = 'preferences.models'

    active_poll = models.ForeignKey(poll_models.PollQuestion, blank=True, null=True)
    active_stock_ticker = models.ForeignKey(
        investor_models.StockTicker,
        blank=True,
        null=True
    )
    active_social_media = models.ForeignKey(SocialMedia, blank=True, null=True)

    class Meta:
        verbose_name = 'site preference'
        verbose_name_plural = 'site preferences'
