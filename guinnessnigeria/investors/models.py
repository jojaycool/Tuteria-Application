from django.db import models


class StockTicker(models.Model):
    current_stock_value = models.DecimalField(max_digits=7, decimal_places=2)
    previous_stock_value = models.DecimalField(max_digits=7, decimal_places=2)
    last_updated = models.DateField(auto_now=True)

    @property
    def percentage_difference(self):
        return ((self.current_stock_value - self.previous_stock_value) / self.previous_stock_value) * 100  # noqa

    @property
    def percentage_difference_color(self):
        return "red" if self.percentage_difference < 0 else "green"

    def __unicode__(self):
        return u'%0.2f' % self.current_stock_value


class FinancialDownload(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='stock_reports')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % self.title


class ShareSummary(models.Model):
    average_purchase_price = models.DecimalField(max_digits=7, decimal_places=4)
    shares = models.IntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['date']
        verbose_name = 'share summary'
        verbose_name_plural = 'share summaries'

    def __unicode__(self):
        return u'%s' % self.date


class ShareDownload(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='share_downloads')
    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'share download'
        verbose_name_plural = 'share downloads'


class FinancialReport(FinancialDownload):
    pass


class FinancialResult(FinancialDownload):
    pass
