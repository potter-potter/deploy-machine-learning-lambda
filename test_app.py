import json
from unittest import TestCase

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class TestApp(TestCase):
    def setUp(self):
        self.lg = LocalGateway(app, Config())

    def test_get_index(self):
        response = self.lg.handle_request(method='GET',
                                          path='/',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['hello']) == 'friend'

 