#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-19 15:30
# @Author  : 刘开

"""
页面按钮配置
"""

import requests
import pytest
from commen.config import Config

class TestpageButton():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_selectByPageAndButton(self):
        """校验页面按钮配置配置类型页面功能"""
        url = '/crystalBall-web/page/selectByPageAndButton?'
        data = {
            "type": "page",
            "line": "3",
            "region": "40",
            "pageSize":"10",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()["data"]['folders'][0] == {'urlId': '3475360', 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'urlName': '非凡高清首页', 'urlType': None, 'urlLevel': None, 'positionId': None, 'positionName': None, 'staffId': None, 'dataSourceCd': 'dazhong', 'isValid': None, 'displayOrder': None, 'createDate': None, 'updateDate': None, 'expireDate': None, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'positionCode': None, 'rm2': '1', 'rm1': None, 'rm3': None, 'x': None, 'y': None, 'img_URL': 'http://125.210.125.183/crystalBall/upload/20170329/20170329133504.jpg'}


    def test_selectByPageAndButton02(self):
        """校验页面按钮配置页面搜索功能"""
        url = '/crystalBall-web/page/selectByPageAndButton?'
        data = {
            "type": "page",
            "line": "3",
            "region": "40",
            "pageSize":"10",
            "name": "非凡高清首页",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        print(response.json()["data"]['folders'][0])
        assert response.json()["data"]['folders'][0] == {'urlId': '3475360', 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'urlName': '非凡高清首页', 'urlType': None, 'urlLevel': None, 'positionId': None, 'positionName': None, 'staffId': None, 'dataSourceCd': 'dazhong', 'isValid': None, 'displayOrder': None, 'createDate': None, 'updateDate': None, 'expireDate': None, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'positionCode': None, 'rm2': '1', 'rm1': None, 'rm3': None, 'x': None, 'y': None, 'img_URL': 'http://125.210.125.183/crystalBall/upload/20170329/20170329133504.jpg'}


    def test_selectByPageAndButton03(self):
        """校验页面按钮配置按钮搜索功能"""
        url = '/crystalBall-web/page/selectByPageAndButton?'
        data = {
            "type": "button",
            "line": "3",
            "region": "40",
            "pageSize":"10",
            "name": "非凡高清首页",
            "positionCode":"nav1_4",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        print(response.json()["data"]['folders'][0])
        assert response.json()["data"]['folders'][0] == {'urlId': '3475392', 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'urlName': '非凡高清首页', 'urlType': None, 'urlLevel': None, 'positionId': None, 'positionName': '居家办', 'staffId': None, 'dataSourceCd': 'dazhong', 'isValid': None, 'displayOrder': None, 'createDate': None, 'updateDate': None, 'expireDate': None, 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'positionCode': 'nav1_4', 'rm2': '1', 'rm1': None, 'rm3': None, 'x': 250, 'y': 20, 'img_URL': 'http://125.210.125.183/crystalBall/upload/20170329/20170329133504.jpg'}


if __name__ == '__main__':
    pytest.main(['-sv'])