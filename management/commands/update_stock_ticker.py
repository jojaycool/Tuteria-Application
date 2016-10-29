'''
Created on 16 Jan 2013

@author: euan
'''
from django.core.management.base import BaseCommand

from guinnessnigeria.tasks import get_latest_stock_value


class Command(BaseCommand):
    """
    Initial base setup
    """

    def handle(self, *args, **options):
        get_latest_stock_value()
