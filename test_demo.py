import requests


class TestDemo:
    def test_get_token(self):

        r=requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid':'wwf56f991cbbdd11e7',
            'corpsecret':'5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'})
        print(r.json())
        return r.json()['access_token']
#若运行失败在web端重新配置企业可信IP（IP为动态）
    def test_department_list(self):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/department/simplelist',
            params={
                'access_token':self.test_get_token(),
                'id':''
            })
        assert r.json()['errcode'] == 0
        return print(r.json())
