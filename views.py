# -*- coding: utf-8 -*-
"""
Модуль для функций, которые будут возвращать ответ для указанного ресурса.
Ответ - helpers.ResponseØ
"""
import logging

from helpers import Response, DEFAULT_HEADERS, html_render

logger = logging.getLogger(__name__)


def index_view(env, uri):
    body = html_render('index.html', title='Index page', body=f'Стартовая страница тестового uwsgi-сервера')
    return Response(200, DEFAULT_HEADERS, body)


def example_page_view(env, uri):
    body = html_render('example_page.html', title='Example page', uri=uri, method=env["REQUEST_METHOD"])
    return Response(200, DEFAULT_HEADERS, body)
