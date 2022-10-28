# coding:utf-8
import configparser
import os
import json


class HandleInit:
    folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        """
        初始化
        """
        self.cf = configparser.ConfigParser()
        self.file_path=os.path.join(self.folder,'config','config.ini')

        if not os.path.exists(self.file_path):
            raise FileNotFoundError("配置文件不存在，请检查~")

        self.cf.read(self.file_path,encoding='utf-8-sig')



    def get_value(self,key,section=None):
        '''
        获取ini文件中的配置数据
        :return:value
        '''
        if section == None:
            section = "service"
        else:
            section=section
        try:
            data=self.cf.get(section,key)
        except Exception:
            print("no this value")
            data=None
        return data





handle_init=HandleInit()

if __name__ == '__main__':
    data=handle_init.get_value('wechat','service')
    print(data)


