# -*- coding: utf-8 -*-
import logging
import sys

import views
from simple_wsgi import SimpleWSGI

logger = logging.getLogger()

ENABLE_LOG = True


def setup_logger():
    """
    Настройка логирования
    """
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)-35s(ln:%(lineno)04d) %(levelname)-05s: %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


if ENABLE_LOG:
    setup_logger()

application = SimpleWSGI()
application.add_route('', views.index_view, ('GET', ))
application.add_route('example_page', views.example_page_view, ('GET', 'POST', ))
