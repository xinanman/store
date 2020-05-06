# -*- coding: UTF-8 -*-
#_auther:zhangxin
#date : 2020/4/29
import requests
def cookies():
    url='http://t.yadmin.qa.daling.com/dal_yadmin/login.do '
    datas={
        'username':'mengxiangguo',
        'password':'Meng.1'
    }
    data=requests.get(url=url,params=datas)
    return data

if __name__=="__main__":
    aa=cookies()
    print(aa)