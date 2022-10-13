# from department import Department
import pytest

from api.department import Department


class TestDepartment:
    department = Department()
    @pytest.mark.parametrize('id',[2,3,4])
    def test_department_list(self,id):
        r = self.department.list(id)
        print(r)
        assert self.department.jsonpath(expr='$..parentid')[0]== 1