#coding:utf-8

import requests
import json
from common.handle_config import handle_init
import time
from common.handle_logger import MyLog

class Baserequests:

#     单个测试，返回结果

    def get_request(self,url,data):
        '''
        get方法请求
        :param url:
        :param param:
        :param hearder:
        :param cookies:
        :return:
        '''
        if url.startswith('http://') or url.startswith('https://'):
            pass
        else:
            url ='%s%s' % ('http://',url)

        try:
            response=requests.get(url=url,params=data)
        except requests.exceptions.ConnectTimeout:
            raise Exception("ConnectTimeout")
            MyLog().debug("请求链接超时")
        except requests.exceptions.ConnectionError:
            raise Exception("ConnectionError")
            MyLog().debug("请求链接错误")
        except requests.exceptions.RequestException:
            raise Exception("RequestException")
            MyLog().debug("请求失败")

        return response


    def post_request(self,url,params,data,headers):
        '''
        post方法
        :param url:
        :param param:
        :param hearder:
        :return:
        '''
        if url.startswith('http://') or url.startswith('https://'):
            pass
        else:
            url ='%s%s' % ('http://',url)

        try:
            response=requests.post(url=url,params=params,data=data,headers=headers)
            print(response.url)
            print(response.headers)
        except requests.exceptions.ConnectTimeout:
            raise Exception("ConnectTimeout")
            MyLog().debug("请求链接超时")
        except requests.exceptions.ConnectionError:
            raise Exception("ConnectionError")
            MyLog().debug("请求链接错误")
        except requests.exceptions.RequestException:
            raise Exception("RequestException")
            MyLog().debug("请求失败")

        return response



    def put_request(self,url,data):
        '''
        put方法
        :param url:
        :param param:
        :param hearder:
        :return:
        '''
        if url.startswith('http://') or url.startswith('https://'):
            pass
        else:
            url ='%s%s' % ('http://',url)

        try:
            response=requests.put(url=url,data=json.dumps(data))
        except requests.exceptions.ConnectTimeout:
            raise Exception("ConnectTimeout")
        except requests.exceptions.ConnectionError:
            raise Exception("ConnectionError")
        except requests.exceptions.RequestException:
            raise Exception("RequestException")

        return response

    def delete_request(self, url, data):
        '''
        delete方法
        :param url:
        :param param:
        :param hearder:
        :return:
        '''
        if url.startswith('http://') or url.startswith('https://'):
            pass
        else:
            url = '%s%s' % ('http://', url)

        try:
            response = requests.delete(url=url, data=json.dumps(data))
        except requests.exceptions.ConnectTimeout:
            raise Exception("ConnectTimeout")
        except requests.exceptions.ConnectionError:
            raise Exception("ConnectionError")
        except requests.exceptions.RequestException:
            raise Exception("RequestException")

        return response

    def sent_request_response(self,url,method,headers,data,params):
        '''
        根据不同的方法获取response
        :param url:
        :param mothod:
        :param data:
        :param header:
        :return:
        '''
        if method == "get":
            response = self.get_request(url=url, data=data)
        elif method == "post":
            response = self.post_request(url=url, params=params,data=data,headers=headers)
        elif method == "put":
            response = self.put_request(url=url, data=data)
        elif method == "delete":
            response = self.delete_request(url=url, data=data)
        else:
            print("this method is error")
        return response


handle_request=Baserequests()