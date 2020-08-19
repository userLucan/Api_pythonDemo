#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-13 21:46
# @Author  : 刘开
import ast
from Tools.logger import Logger
import requests
import json
from Tools.config import Config
from Tools.execlReader import ExeclReader
from Tools.config import Config
from Tools.TimeGlobal import *
config =Config()
print(year_time())
cookies=ast.literal_eval(config.get_value('cookie.conf','cookies','cookie'))
print(type(cookies))
loger = Logger('SendRequest').getlog()
class SendRequest():

    # 去掉初始化
    @staticmethod
    def request_api(host, url, method, data,cookie):
        test_url = host + url
        # 做一个没加http://的判断
        if not test_url.startswith('http://'):
            test_url = 'http://' + test_url

        # 封装请求方法
        try:
            if method == 'GET':
                # if header is None or header == '':
                # 判断data信息是否为空如果为空请求url，如果不为空请求url以及参数
                datas = json.loads(data)
                if datas is None or datas == '':
                    return requests.get(url=test_url)

                else:
                    if 'token'not in datas:
                        if datas['from'] !=day_time('day'):
                            if datas['end']!=day_time('day'):
                                datas['token']=config.get_value('cookie.conf','cookies','token')
                                datas['from'] = day_time('day')
                                datas['end'] = day_time('day')
                                return requests.get(url=test_url,params=datas)

            elif method == 'POST':
                # if header is None or header == '':
                if data is None or data == '':
                    return requests.post(url=test_url)
                else:
                    return requests.post(url=test_url,data=data,headers=cookie)


        except Exception as f:
            loger.error('服务器异常请排查',f)


if __name__ == '__main__':
    #初始化配置文件，读取表格
    config = Config()
    file = 'global_analysis.xlsx'
    execl = ExeclReader(file, 1)
    testdata = execl.get_execl_index()
    print(testdata)
    # 发送sendrequest请求
    send = SendRequest()
    host = config.get_value('host.conf','dev','host')
    print(type(host))
    for lens in testdata:
        res=send.request_api(host,lens['url'],lens['method'],lens['data'],cookie=cookies)
        # rest=json.dumps(res.json())
        print(res.json()['data'])
        print(type(lens['expect']))
        assert len(res.json()['data'])>=1

