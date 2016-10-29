from django.db import models

from unobase import models as unobase_models


class PressRelease(unobase_models.ContentModel, unobase_models.StateModel):
    """
    This is my press release model to store press releases.
    """

    class Meta:
        ordering = ['-publish_date_time']


class Publication(models.Model):
    publication_date = models.DateField()
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='publications')

    class Meta:
        ordering = ['-publication_date']

    def __unicode__(self):
        return u'%s' % self.title
