#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-19 15:09
# @Author  : 刘开

"""
月访问构成天数
"""


import requests
import pytest
from commen.config import Config

class TestvisitComposition():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_visit(self):
        """校验月访问天数构成占比"""
        url = '/crystalBall-web/page/visit?'
        data = {
            "time": "202007",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['img'][0] == {'date': {'a': 27320, 'b': 46169, 'c': 31905, 'd': 25449, 'e': 26144, 'f': 31731, 'g': 124167}, 'cycleId': '202007'}
        assert response.json()['data']['list'][0] == {'visitdayCnt': 1, 'cycleId': '202007', 'visitUserCnt': 27320}


    def test_visit01(self):
        """校验月访问天数地区三构成占比"""
        url = '/crystalBall-web/page/visit?'
        data = {
            "time": "202007",
            "line": "3",
            "region": "1001",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['img'][0] == {'date': {'a': 14385, 'b': 23778, 'c': 16831, 'd': 13820, 'e': 14655, 'f': 17927, 'g': 78828}, 'cycleId': '202007'}
        assert response.json()['data']['list'][0] == {'visitdayCnt': 31, 'cycleId': '202007', 'visitUserCnt': 42678}



if __name__ == '__main__':
    pytest.main(['sv'])
