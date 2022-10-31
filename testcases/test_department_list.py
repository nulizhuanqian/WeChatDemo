# from department import Department
import json

import pytest
import yaml

from api.department import Department
from common.handle_config import handle_init
from common.handle_request import handle_request
from common.handle_yaml import yaml_init


class TestDepartment:
    #  department = Department()
    #  @pytest.mark.parametrize('id',yaml.safe_load(open('../data/department_list.yml',encoding='utf-8'))
    # )
    #  def test_department_list(self,id):
    #      r = self.department.list(id)
    #      print(r)
    #      assert self.department.jsonpath(expr='$..parentid')[0]== 1

    data_case = '/department_list.yml'
    # headers = {"Content-Type": "application/json"}
    @pytest.mark.parametrize('case', yaml_init.read_yamls(data_case))
    def test_department_list(self, case, get_base_url, get_access_token):
        base_url = get_base_url
        # print(type(case))
        for i in case:
            if 'create' in i:
                url = base_url + case[i]['url']+get_access_token
                method = case[i]['method']
                data = case[i]['body']
                # print(type(data))
                # print(data)
                res_insert = handle_request.sent_request_response(url, method,data)
                # print(res_insert.request.body)
                # print(type(res_insert.request.body))
                # print(res_insert.json())
                assert (case[i]['expect']['errcode'] == res_insert.json()['errcode'])
