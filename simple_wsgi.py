# -*- coding: utf-8 -*-
import logging

from helpers import Response, DEFAULT_HEADERS, html_render

logger = logging.getLogger(__name__)


class SimpleWSGI:
    def __init__(self, routes_without_slash=True):
        """
        :param routes_without_slash: требуется ли убирать слеши из ресурсов
        """
        self.routes = {}
        self.uri = ''
        self.req_method = ''
        self.routes_without_slash = routes_without_slash

    def __call__(self, env, start_response):
        """
        Делаем объект вызываемым - требуется для работы uWSGI

        :param env: данные запроса
        :param start_response: функция для возврата кода и хедеров
        :return: тело ответа
        """
        logger.debug(f'Зарос: {env}')
        self.uri = env['PATH_INFO'].strip('/') if self.routes_without_slash else env['PATH_INFO']
        self.req_method = env['REQUEST_METHOD']
        logger.debug(f'uri: {self.uri}')
        logger.debug(f'req_method: {self.req_method}')
        logger.debug(f'Настроенные пути: {self.routes}')
        if self.uri in self.routes:
            if self.req_method in self.routes[self.uri]['methods']:
                response = self.routes[self.uri]['view'](env, self.uri)
            else:
                response = self._method_not_allowed_response()
        else:
            response = self._not_found_response()

        start_response(response.code_for_wsgi, response.headers_for_wsgi)
        return response.body

    def add_route(self, route: str, view: callable, methods: tuple):
        """
        Добавить обработку ресурса

        :param route: ресурс
        :param view: функция для возврата ответа. Функция должна возвращать объект helpers.Response
        :param methods: доступные методы для ресурса
        """
        route = route.strip('/') if self.routes_without_slash else route
        self.routes[route] = {'view': view, 'methods': methods}

    def _not_found_response(self):
        """
        Возврат ответа, когда вызываемый ресурс не найден
        """
        return Response(404, DEFAULT_HEADERS, html_render('error_page.html', title='404 page', main_text='404 error',
                                                          ext_text=f'Ресурс "{self.uri}" не найден'))

    def _method_not_allowed_response(self):
        """
        Возврат ответа, когда вызываемый метод не поддерживается для ресурса
        """
        return Response(405, DEFAULT_HEADERS, html_render('error_page.html', title='405 page', main_text='405 error',
                                                          ext_text=f'Метод "{self.req_method}" недоступен '
                                                          f'для ресурса "{self.uri}"'))
