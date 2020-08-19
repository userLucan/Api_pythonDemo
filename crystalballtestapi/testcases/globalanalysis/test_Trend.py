#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-04 15:53
# @Author  : 刘开
# 趋势分析


import requests
import pytest

from commen.config import Config


class TestAnalysis():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_01(self):
        """检查趋势分析按时天查询"""
        url = '/crystalBall-web/overall/trendByHour?from=20200803&end=20200803&line=3&region=10&token=' + self.config.get_value(
            'cookie.conf',
            'token', 'token')
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url)
        print(response.json()["data"])
        assert len(response.json()['data']) >= 1

    def test_02(self):
        """校验按周查询"""
        url = '/crystalBall-web/overall/realByMin?'
        data = {
            "from": "20200727",
            "end": "20200802",
            "line": "3",
            "region": "10",
            "token": self.config.get_value('cookie.conf','token','token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url,params=data)
        assert len(response.json()['data']) >= 1

    def test_03(self):
        """校验按天查询"""
        url = '/crystalBall-web/overall/realByMin?'
        data = {
            "from": "20200801",
            "end": "20200801",
            "line": "3",
            "region": "10",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert len(response.json()['data']) >= 1

    def test_04(self):
        """校验按月(月)查询"""
        url = '/crystalBall-web/overall/realByMin?'
        data = {
            "end": "202007",
            "line": "3",
            "region": "1001",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert len(response.json()['data']) >= 1
if __name__ == '__main__':
    #pytest.main(['-sv test_Trend.py'])

    pytest.main(['../testcases/', '--html=../report/report.html'])
