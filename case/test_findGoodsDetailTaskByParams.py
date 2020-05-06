# -*- coding: UTF-8 -*-
#_auther:zhangxin
#date : 2020/3/31

import json
import allure
import pytest
import requests
from dutil.res_diff import res_diff
from dutil.find_case import findCase
from dutil.make_ddt import MakeDdt
from conf.sysconfig import HOST

casepath = findCase(__file__, 'findGoodsDetailTaskByParams.yml')
test_cases = MakeDdt(casepath).makeData()

class TesttestFindGoodsDetailTaskByParams():
    @allure.title("查询商详页展示任务说明")
    @pytest.mark.parametrize("method, url, params, data,headers,cookies, proxies, status_code, expectData", test_cases)
    
    def test_findGoodsDetailTaskByParams(self, method, url, params, data, headers, cookies, proxies, status_code,expectData):
        '''品牌收藏'''
        url = HOST + '/dal_task_system_cur_server/server/taskSystemCurController/findGoodsDetailTaskByParams'
        res = requests.get(url, headers=headers, params={'sku':'111111'})
        print(res.json())
        assert {} == res_diff(expectData, res.json())