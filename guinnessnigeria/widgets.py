'''
Created on 22 Aug 2013

@author: michael
'''
import datetime
from django.forms import widgets


class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        days = [(year, year) for year in range(1, 32)]
        months = [(year, year) for year in range(1, 13)]
        years = [(year, year) for year in range((datetime.datetime.now() - datetime.timedelta(days=73*365)).year,  # noqa
                                                            (datetime.datetime.now() - datetime.timedelta(days=17*365)).year)]  # noqa
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]

        try:
            D = datetime.date(
                day=int(datelist[0]),
                month=int(datelist[1]),
                year=int(datelist[2])
            )
        except ValueError:
            return ''
        else:
            return D
