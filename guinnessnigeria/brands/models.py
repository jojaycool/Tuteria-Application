from django.db import models

from unobase import models as unobase_models


class BrandCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'brand category'
        verbose_name_plural = 'brand categories'

    def __unicode__(self):
        return u'%s' % self.name


class Brand(unobase_models.ContentModel, unobase_models.StateModel):
    category = models.ManyToManyField(
        BrandCategory,
        through='BrandCategoryThrough',
        related_name='brands',
        blank=True,
        null=True
    )
    associated_brand = models.ForeignKey(
        'self',
        related_name='associated_brands',
        blank=True,
        null=True
    )
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_first_category(self):
        if self.category.all().count():
            return self.category.all()[0]


class BrandCategoryThrough(models.Model):
    brand_category = models.ForeignKey(BrandCategory)
    brand = models.ForeignKey(Brand)

    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)
