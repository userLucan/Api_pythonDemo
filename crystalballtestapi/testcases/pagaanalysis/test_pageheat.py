#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-18 16:18
# @Author  : 刘开

"""
页面热体图
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

    def test_getHeatMapByMonth(self):
        """页面热体图校验"""
        url = '/crystalBall-web/page/getHeatMapByMonth?'
        data = {
            "from": "202007",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] == {'cycleId': '202007', 'url': None, 'urlName': '非凡高清首页', 'positionId': 0, 'positionName': '应用中心', 'positionCnt': 3407, 'positionUserCnt': 2036, 'x': 600, 'y': 200, 'img_URL': 'http://125.210.125.183/crystalBall/upload/20170329/20170329133504.jpg', 'newPositionCnt': 6}

    def test_getHeatMapByMonth01(self):
        """页面热体图地区三校验"""
        url = '/crystalBall-web/page/getHeatMapByMonth?'
        data = {
            "from": "202007",
            "line": "3",
            "region": "1001",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] =={'cycleId': '202007', 'url': None, 'urlName': '非凡高清首页', 'positionId': 0, 'positionName': '应用中心', 'positionCnt': 1784, 'positionUserCnt': 1066, 'x': 600, 'y': 200, 'img_URL': 'http://125.210.125.183/crystalBall/upload/20170329/20170329133504.jpg', 'newPositionCnt': 5}

if __name__ == '__main__':
    pytest.main(['sv'])