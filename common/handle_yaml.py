
# @Author: HanXiaoqing
# @Time : 2020/10/30
# FileName: handle_yaml.py


import yaml
import json
import os.path
import time

#获取配置文件路径
path_yaml= os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))+'/data'

class Handle_yaml:
    '''
    获取yaml配置文件数据
    '''
    def read_yaml(self,file_name,mode= 'r'):
        try:
            with open(path_yaml+file_name, mode, encoding='utf-8') as f:
                #由于yaml.load()支持原生python 对象，不安全，建议使用yaml.safe_load()
                return yaml.safe_load(f)
        except Exception as e:
            print(file_name, "file read is error", e)




    def write_yaml(self,file_name,api_name,key,value):
        '''
        编辑yaml文件
        :param file_name:
        :param key:
        :param value:
        :return:
        '''
        try:
            self.content=self.read_yaml(file_name)
            #修改yaml文件中都参数
            self.content[api_name]['body'][key] = value
            time.sleep(1)
            with open(path_yaml + file_name, 'w', encoding='utf-8') as nf:
                yaml.safe_dump(self.content,nf,default_flow_style=False,allow_unicode=True)
            return True
        except Exception as e:
            print(file_name, "file write is error", e)
            return False


    def read_yamls(self,file_name,mode='r'):
        try:
            with open(path_yaml+file_name,mode,encoding='utf-8') as f:
                content=yaml.load_all(f, Loader=yaml.FullLoader)#读取文件，并且以字典的形式存放
                data_list=[]
                for i in content:
                    print(type(i))
                    print(i)
                    data_list.append(i)
                return data_list
        except Exception as e:
            print(file_name, "file read is error", e)



yaml_init=Handle_yaml()



if __name__ == '__main__':
    # print(yaml_init.read_yamls('/department_list.yml'))
    base_url='https://qyapi.weixin.qq.com/cgi-bin/department/'
    list = yaml_init.read_yamls('/department_list.yml')
    for param in list:
        if 'create' in param:
            url= base_url+list[param]['url']
            method=list[param]['method']
            json_param = list[param]['body']
            print(url)
        # print(i)
    # print(path_yaml)
    # yaml_init.write_yaml("/ceboshi/GroupController/insertGroup.yaml", "group_update", "groupCode", "11111")
    # data=yaml_init.read_yaml("/ceboshi/SmsCoupon/CouponController.yaml")
    # # print(data)
    # # print(type(data))
    # # print(data[0])
    # # print(data[0]['insert_smscoupon'])
    # # # insert,update,group_list,group_listaspage,group_listaspagebygroupname,group_update,select_listBees=data
    # # # print(insert)
    # # # print(data[0]['insert_smscoupon_discount'])
    # # # print(type(str(data[0]['insert_smscoupon_discount']['except']['message'])))
    # # # for i in data:
    # # #
    # # #     print(i['insert_smscoupon_discount']['except']['message'])
    # # #     print(type(i['insert_smscoupon_discount']['except']['message']))
    # print(data)
    # print(data['insert_smscoupon']['url'])
    # print(type(data['insert_smscoupon']))
    # print(type(data['insert_smscoupon']['url']))
    # print(type(data['insert_smscoupon']['body']))
