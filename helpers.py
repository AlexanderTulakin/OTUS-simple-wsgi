# -*- coding: utf-8 -*-
import logging
import pathlib

from jinja2 import Template

logger = logging.getLogger(__name__)

DEFAULT_HEADERS = {'Content-Type': 'text/html'}


class Response:
    """
    Класс для ответа
    """
    HTTP_CODES = {200: 'OK',
                  400: 'Bad Request',
                  404: 'Not Found',
                  405: 'Method Not Allowed',
                  }

    def __init__(self, code: int, headers: dict, body: str):
        self.code = code
        self.headers = headers
        self.body = [body.encode("utf-8")]
        self.code_for_wsgi = self._code_transform()
        self.headers_for_wsgi = self._headers_transform()

    def _code_transform(self):
        """
        Преобразование кода ответа, в строку вида "{код} {текстовое описание}"
        """
        code_text = self.HTTP_CODES.get(self.code, '')
        return f'{self.code} {code_text}'

    def _headers_transform(self):
        """
        Преобразование словаря из заголовков в список из кортежей
        :return:
        """
        return list(self.headers.items())


def html_render(template, **kwargs):
    """
    Рендер http шаблона
    """
    path = f'templates/{template}'
    html = pathlib.Path(path).read_text()
    template = Template(html)
    return template.render(**kwargs)
