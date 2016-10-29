from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    external_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'
