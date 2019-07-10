#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

from .utils import readAPICreds


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            inst = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = inst
        return cls._instances[cls]


class trelloConn(object, metaclass=Singleton):
    """
    Trello Connection - Base class for Trello API access.
    """

    def __init__(self, api_key=None, token=None):
        """
        Constructor

        :api_key: API key generated at  https://trello.com/app-key
        :token: OAuth token generated by the user in
                    trello.util.create_oauth_token
        """
        cred = readAPICreds()
        self.api_key = api_key or cred['api_key']
        self.token = token or cred['token']

    def execute(self, uri_path, query_params={}, http_method="GET"):
        """
        Wrapper to execute a request to Trello and execute an operation

        :uri_path:      endpoint to request the service
        :http_method:   method to request. Default is GET

        """
        # set headers to handle JSON
        headers = {}
        if http_method in ("POST", "PUT", "DELETE"):
            headers['Content-Type'] = 'application/json; charset=utf-8'

        headers['Accept'] = 'application/json'

        # construct the full URL without query parameters
        if uri_path.startswith("/"):
            uri_path = uri_path[1:]
        if uri_path.endswith("/"):
            uri_path = uri_path[:-1]
        url = 'https://api.trello.com/1/%s' % uri_path

        # set parameters to send in url
        query_params['key'] = self.api_key
        query_params['token'] = self.token

        # EXECUTE the HTTP requests
        response = requests.request(http_method, url, params=query_params,
                                    headers=headers)

        if response.status_code != 200:
            response.raise_for_status()
            return []

        return response.text

    def get(self, uri_path, query_params={}):
        """
        Wrapper to execute a GET request to Trello

        :uri_path:      endpoint to request the service
        """
        return self.execute(uri_path, query_params, "GET")

    def post(self, uri_path, query_params):
        """
        Wrapper to execute a POST request to Trello

        :uri_path:      endpoint to request the service
        :query_params:  dictionary containing the parameters to send in POST
        """
        return self.execute(uri_path, query_params, "POST")

if __name__ == "__main__":
    print
