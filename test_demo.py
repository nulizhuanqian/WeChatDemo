import json

import requests


class TestDemo:

    # 获取access_token
    def test_get_token(self):

        r=requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid':'wwf56f991cbbdd11e7',
            'corpsecret':'5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'})
        print(r.json())
        return r.json()['access_token']


        # 获取子部门列表
        # 若运行失败在web端重新配置企业可信IP（IP为动态）
    def test_department_list(self):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/department/simplelist',
            params={
                'access_token':self.test_get_token(),
                'id':''
            })
        print(r.json())
        assert r.json()['errcode'] == 0
        return print(r.json())


    # 创建部门
    def test_create_department(self):

        r=requests.post(
            url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
             params={'access_token':self.test_get_token()},
             json={
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
                "id": 5

        })
        assert r.json()["errcode"] == 0



    #     更新部门
    def test_update_department(self):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/department/update',
            params = {'access_token': self.test_get_token()},
            # 如果非必须的字段未指定，则不更新该字段
            json = {
                    "id": 5,
                    "name": "广州研发中心",
                    "name_en": "RDGZ",
                    "parentid": 1,
                    "order": 1
            }
        )
        print(r.url)

    def test_create_department1(self):
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 5

        }
        r=requests.post(
            url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
            params={'access_token':self.test_get_token()},
            data=json.dumps(data))
        assert r.json()["errcode"] == 0

    # 删除部门（不能删除根部门，不能删除含有子部门，成员的部门）
    def test_delete_department(self):
        r = requests.get(
            url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete',
            params = {'access_token': self.test_get_token(), 'id':5}
        )
        assert r.json()["errcode"] == 0





