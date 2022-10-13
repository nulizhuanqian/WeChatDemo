import requests

from api.wework import WeWork


class Department(WeWork):
    list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/simplelist'
    def list(self, id):
        # print(WeWork.get_access_token(self))
        access_token = WeWork.get_access_token(self).json()['access_token']
        # print(access_token)
        self.json_data = requests.get(
            self.list_url,
            params={'access_token': access_token,
                    'id': id}).json()
        # print(self.json_data)
        return self.json_data


