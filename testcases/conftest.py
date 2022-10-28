# coding:utf-8
# @Author: HanXiaoqing
# @Time : 2021/1/14
# FileName: conftest.py

from common.handle_config import handle_init
from common.handle_request import handle_request
import json
import requests
import pytest
import datetime


# 登录接口获取token
@pytest.fixture(scope='class')
# 获取access_token
def get_access_token():
    r = requests.get(
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': 'wwf56f991cbbdd11e7',
                'corpsecret': '5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'})
    params_dic={'access_token':r.json()['access_token']}
    return params_dic

@pytest.fixture(scope='class')
def get_base_url():
    base_url=handle_init.get_value('wechat', 'service')
    return base_url


# @pytest.fixture(scope='class')
# def test_get_token():
#     r = requests.get(
#         url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
#         params={'corpid': 'wwf56f991cbbdd11e7',
#                 'corpsecret': '5okJWMCCzFT9hIxuxVUw5ORAwkf7WjjPK1q_E1dv09g'})
#     get_access_token=r.json()['access_token']
#     headers = {
#         "Content-type": "application/json"
#     }
#     return headers,get_access_token



if __name__ == '__main__':
    print(type(handle_init.get_value('wechat','service')))
    print(handle_init.get_value('wechat','service'))