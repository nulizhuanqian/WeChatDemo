import requests as requests

from api.base_api import BaseApi


class WeWork(BaseApi):
    corp_id = 'wwf56f991cbbdd11e7'
    contact_secret = '5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'
    token = dict()
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

    def get_access_token(self):
        r = self.request(
            method='get',url=self.token_url,
            params={'corpid': self.corp_id,
                    'corpsecret':self.contact_secret}
        )
        return r




    #
    # @classmethod
    # def get_token(cls, secret=contact_secret):
    #     if secret not in cls.token.keys():
    #         r = cls.get_access_token(secret)
    #         cls.token[secret] = r['access_token']
    #     return cls.token[secret]
    #
    # @classmethod
    # def get_access_token(cls, secret):
    #     r = requests.get(cls.token_url, params={'cordid': cls.corp_id, 'corpsecret': secret})
    #     return r.json()
