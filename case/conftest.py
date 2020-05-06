#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Meng xiangguo <mxgnene01@gmail.com>
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                        2019-09-17  14:31

import pytest
import requests
from dutil.xc_auth import getUserHeaders
from conf.sysconfig import UC_DB
from conf.sysconfig import UC_HOST


# 达令家 auth 鉴权
@pytest.fixture(scope='session')
def dheaders(request):
    headers = getUserHeaders(request.param, UC_DB, UC_HOST)
    return headers

# @pytest.fixture(scope='session')
def cookies():
    url='http://t.yadmin.qa.daling.com/dal_yadmin/login.do '
    datas={
        'username':'mengxiangguo',
        'password':'Meng.1'
    }
    data=requests.get(url=url,params=datas)
    return data
    
if __name__=="__main__":
    cookies()




