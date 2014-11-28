"""ArangoDB Request Client."""

import json
import requests
from arango.util import unicode_to_str

class Connection(object):
    """A simple wrapper for making HTTP requests to ArangoDB.

    :param protocol: the internet transfer protocol (default: http).
    :type protocol: str.
    :param host: ArangoDB host (default: localhost).
    :type host: str.
    :param port: ArangoDB port (default: 8529).
    :type port: int.
    :param username: username for ArangoDB (default: root).
    :type username: str.
    :param password: password for ArangoDB (default: empty string).
    :type password: str.
    :param db_name: the database to make the requests to (default: _system)
    :type db_name: str.
    """

    def __init__(self, protocol="http", host="localhost", port=8529,
                 username="root", password="", db_name="_system"):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

    @property
    def _url_prefix(self):
        """Generate and return the URL prefix."""
        return "{protocol}://{host}:{port}/_db/{db}".format(
            protocol = self.protocol,
            host = self.host,
            port = self.port,
            db = self.db_name,
        )

    def head(self, path, **kwargs):
        """Execute an HTTP HEAD method."""
        res = requests.head(self._url_prefix + path,
                            auth=(self.username, self.password),
                            **kwargs)
        return res

    def get(self, path, **kwargs):
        """Execute an HTTP GET method."""
        res = requests.get(self._url_prefix + path,
                           auth=(self.username, self.password),
                           **kwargs)
        res.obj = unicode_to_str(res.json()) if res.text else None
        return res

    def put(self, path, data=None, **kwargs):
        """Execute an HTTP PUT method."""
        res = requests.put(self._url_prefix + path,
                           data="" if data is None else json.dumps(data),
                           auth=(self.username, self.password),
                           **kwargs)
        res.obj = unicode_to_str(res.json()) if res.text else None
        return res

    def post(self, path, data=None, **kwargs):
        """Execute an HTTP POST method."""
        res = requests.post(self._url_prefix + path,
                            data="" if data is None else json.dumps(data),
                            auth=(self.username, self.password),
                            **kwargs)
        res.obj = unicode_to_str(res.json()) if res.text else None
        return res

    def patch(self, path, data=None, **kwargs):
        """Execute an HTTP PATCH method."""
        res = requests.patch(self._url_prefix + path,
                             data="" if data is None else json.dumps(data),
                             auth=(self.username, self.password),
                             **kwargs)
        res.obj = unicode_to_str(res.json()) if res.text else None
        return res

    def delete(self, path, **kwargs):
        """Execute an HTTP DELETE method."""
        res = requests.delete(self._url_prefix + path,
                              auth=(self.username, self.password),
                              **kwargs)
        res.obj = unicode_to_str(res.json()) if res.text else None
        return res