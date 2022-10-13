import requests

from api.wework import WeWork


class TestWeWork():

    def setup_class(self):
        self.wework = WeWork()

    def test_get_access_token(self):
        # contact_secret = '5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'
        r = self.wework.get_access_token().json()
        print(r)
        assert r['errcode'] == 0
