import requests

from utils.utils import Utils


class BaseApi:
    json_data = None

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)

    def request(self, method, url, **kwargs):
        self.json_data = requests.request(method=method, url=url, **kwargs)
        return self.json_data
