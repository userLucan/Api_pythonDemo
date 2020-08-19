#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-18 15:39
# @Author  : 刘开

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

    def test_pagetrendByHour(self):
        """趋势分析按时校验"""
        url = '/crystalBall-web/page/pagetrendByHour?'
        data = {
            "from": "20200817",
            "end": "20200817",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] == {'id': None, 'cycleId': '01:00', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': None, 'pv': 3492, 'uv': 2597, 'bgRate': 0.3853, 'visitTime': None, 'visitPerTime': 63.2, 'gxVisitCnt': 6113, 'newCnt': None, 'positionName': None, 'positionId': None, 'positionCnt': None, 'positionUserCnt': None, 'etlDate': None, 'analysisType': None, 'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None, 'y': None}

    def test_pagetrendByDay(self):
        """趋势分析按日校验"""
        url = '/crystalBall-web/page/pagetrendByDay?'
        data = {
            "from": "20200817",
            "end": "20200817",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] == {'id': None, 'cycleId': '20200817', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': None, 'pv': 413765, 'uv': 169046, 'bgRate': 0.9804, 'visitTime': None, 'visitPerTime': 91.47, 'gxVisitCnt': 709528, 'newCnt': None, 'positionName': None, 'positionId': None, 'positionCnt': None, 'positionUserCnt': None, 'etlDate': None, 'analysisType': None, 'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None, 'y': None}

    def test_pagetrendByWeek(self):
        """趋势分析按周校验"""
        url = '/crystalBall-web/page/pagetrendByWeek?'
        data = {
            "from": "20200810",
            "end": "20200816",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] =={'id': None, 'cycleId': '20200810至20200816', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': None, 'pv': 2934467, 'uv': 239705, 'bgRate': 0.9864, 'visitTime': None, 'visitPerTime': 485.24, 'gxVisitCnt': 5154822, 'newCnt': None, 'positionName': None, 'positionId': None, 'positionCnt': None, 'positionUserCnt': None, 'etlDate': None, 'analysisType': None, 'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None, 'y': None}

    def test_pagetrendByMonth(self):
        """趋势分析按月校验"""
        url = '/crystalBall-web/page/pagetrendByMonth?'
        data = {
            "from": "202007",
            "end": "202007",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data'][0] == {'id': None, 'cycleId': '202007', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': None, 'pv': 14294086, 'uv': 312885, 'bgRate': 0.9871, 'visitTime': None, 'visitPerTime': 2164.66, 'gxVisitCnt': 24422859, 'newCnt': None, 'positionName': None, 'positionId': None, 'positionCnt': None, 'positionUserCnt': None, 'etlDate': None, 'analysisType': None, 'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None, 'y': None}



if __name__ == '__main__':
    pytest.main(['sv'])