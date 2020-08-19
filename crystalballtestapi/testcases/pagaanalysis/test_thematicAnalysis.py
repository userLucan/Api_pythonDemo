#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-19 13:21
# @Author  : 刘开
"""
专题分析
"""


import requests
import pytest
from commen.config import Config

class TesttrendAnalysis():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_ztListByDay(self):
        """专题分析校验"""
        url = '/crystalBall-web/page/ztListByDay?'
        data = {
            "from": "20200812",
            "end": "20200819",
            "line": "3",
            "region": "40",
            "type": "1",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "name":"",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] == {'id': 1, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'subjectId': None, 'subjectName': '美国军机逼近东海', 'subjectCode': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html_nav5_1', 'subjectType': None, 'subjectUrlId': None, 'subjectUrl': 'f=aaa_001_018&assettype=13&assetid=1090112521', 'urlId': None, 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'positionId': 3475448, 'positionCode': 'nav5_1', 'createDate': '20200818', 'expireDate': None, 'pv': 3325, 'uv': 2999, 'etlDate': None, 'createMonth': None, 'urlName': '非凡高清首页', 'positionName': '头条文字位1'}

    def test_ztListByDay01(self):
        """专题分析按钮名称校验"""
        url = '/crystalBall-web/page/ztListByDay?from=20200812&end=20200819&line=3&region=40&postionId=3475448&type=1&url=http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html&name=&token=2fa33282-57c8-41d6-8216-0dbb434b8314&pageIndex=1&pageSize=20&_=1597814427928'
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url)
        print(response.json()['data']['folders'][0])
        assert response.json()['data']['folders'][0] =={'id': 1, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'subjectId': None, 'subjectName': '美国军机逼近东海', 'subjectCode': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html_nav5_1', 'subjectType': None, 'subjectUrlId': None, 'subjectUrl': 'f=aaa_001_018&assettype=13&assetid=1090112521', 'urlId': None, 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'positionId': 3475448, 'positionCode': 'nav5_1', 'createDate': '20200818', 'expireDate': None, 'pv': 3325, 'uv': 2999, 'etlDate': None, 'createMonth': None, 'urlName': '非凡高清首页', 'positionName': '头条文字位1'}

    def test_ztListByDay02(self):
        """专题分析专题名称校验"""
        url = '/crystalBall-web/page/ztListByDay?'
        data = {
            "from": "20200812",
            "end": "20200819",
            "line": "3",
            "region": "40",
            "type": "1",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "name":"美国军机逼近东海",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] == {'id': 1, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'subjectId': None, 'subjectName': '美国军机逼近东海', 'subjectCode': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html_nav5_1', 'subjectType': None, 'subjectUrlId': None, 'subjectUrl': 'f=aaa_001_018&assettype=13&assetid=1090112521', 'urlId': None, 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'positionId': 3475448, 'positionCode': 'nav5_1', 'createDate': '20200818', 'expireDate': None, 'pv': 3325, 'uv': 2999, 'etlDate': None, 'createMonth': None, 'urlName': '非凡高清首页', 'positionName': '头条文字位1'}

    def test_ztListByDay03(self):
        """专题分析专题URL校验"""
        url = '/crystalBall-web/page/ztListByDay?'
        data = {
            "from": "20200812",
            "end": "20200819",
            "line": "3",
            "region": "40",
            "type": "2",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "name": "f=aaa_001_018",
            "ssettype":"13",
            "assetid": "1090112521",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] =={'id': 1, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'subjectId': None, 'subjectName': '美国军机逼近东海', 'subjectCode': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html_nav5_1', 'subjectType': None, 'subjectUrlId': None, 'subjectUrl': 'f=aaa_001_018&assettype=13&assetid=1090112521', 'urlId': None, 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'positionId': 3475448, 'positionCode': 'nav5_1', 'createDate': '20200818', 'expireDate': None, 'pv': 3325, 'uv': 2999, 'etlDate': None, 'createMonth': None, 'urlName': '非凡高清首页', 'positionName': '头条文字位1'}



if __name__ == '__main__':
    pytest.main(['sv'])