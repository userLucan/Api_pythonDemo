#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-13 16:00
# @Author  : 刘开

"""
页面列表
"""

import requests
import pytest
from commen.config import Config


class TestPageList():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_pageListByDay2(self):
        """页面分析日报表页面校验"""
        url = '/crystalBall-web/page/pageListByDay2?'
        data = {
            "from": "20200813",
            "end": "20200813",
            "line": "3",
            "region": "10",
            "positionId": "",
            "type": "page",
            "name": "",
            "token": self.config.get_value('cookie.conf', 'token', 'token'),
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597391197062"}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] == {'id': None, 'cycleId': '20200813', 'ownCorpStdOrgCode': None,
                                                         'stdProdLineVerCode': None, 'monthItvType': None,
                                                         'vocation': None, 'url': 'index', 'urlType': None,
                                                         'urlLevel': None, 'urlName': '省网4.0门户', 'pv': 1342910,
                                                         'uv': 482976, 'bgRate': 0.9377, 'visitTime': None,
                                                         'visitPerTime': 89.8, 'gxVisitCnt': 2749985, 'newCnt': None,
                                                         'positionName': None, 'positionId': None, 'positionCnt': None,
                                                         'positionUserCnt': None, 'etlDate': None, 'analysisType': None,
                                                         'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None,
                                                         'y': None}

    def test_pageListByWeek2(self):
        """页面分析周报表详情页面校验"""
        url = '/crystalBall-web/page/pageListByWeek2?'
        data = {
            "from": "20200810",
            "end": "20200817",
            "line": "3",
            "region": "10",
            "positionId": "",
            "type": "detail",
            "name": "",
            "token": self.config.get_value('cookie.conf', 'token', 'token'),
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597391197062"}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] == {'id': None, 'cycleId': '20200810至20200816', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': '112_1_211', 'urlType': '15', 'urlLevel': None, 'urlName': '综艺--乘风破浪的姐姐', 'pv': 60311, 'uv': 30306, 'bgRate': 0.0367, 'visitTime': None, 'visitPerTime': 23.78, 'gxVisitCnt': 100015, 'newCnt': None, 'positionName': None, 'positionId': None, 'positionCnt': None, 'positionUserCnt': None, 'etlDate': None, 'analysisType': None, 'gltjRate': 0.0, 'vodRate': 2.0, 'img_URL': None, 'x': None, 'y': None}

    def test_pageListByMonth2(self):
        """页面分析月报表按钮名称校验"""
        url = '/crystalBall-web/page/pageListByMonth2?'
        data = {
            "from": "202007",
            "end": "202007",
            "line": "3",
            "region": "40",
            "positionId": "3475440",
            "type": "button",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "token": self.config.get_value('cookie.conf', 'token', 'token'),
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597391197062"}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        print(response.json()['data']['folders'][0])
        assert response.json()['data']['folders'][0] == {'id': None, 'cycleId': '202007', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': 'http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html', 'urlType': None, 'urlLevel': None, 'urlName': '非凡高清首页', 'pv': None, 'uv': None, 'bgRate': None, 'visitTime': None, 'visitPerTime': None, 'gxVisitCnt': None, 'newCnt': None, 'positionName': 'E直播', 'positionId': None, 'positionCnt': 281330, 'positionUserCnt': 37773, 'etlDate': None, 'analysisType': None, 'gltjRate': None, 'vodRate': None, 'img_URL': None, 'x': None, 'y': None}

    def test_upDownByDay(self):
        """页面分析日报表页面上下游校验"""
        url = '/crystalBall-web/page/upDownByDay?'
        data = {
            "time": "20200817",
            "line": "3",
            "region": "40",
            "url": "1087507889",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        # assert response.json()['data']['down'][0]=={'id': None, 'cycleId': '20200817', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': '/template_images/html/search/peopledetails.html?personid=1039467777&aod=谭松韵', 'befUrl': None, 'befUrlType': None, 'befUrlLevel': None, 'befUrlName': None, 'befUrlPv': None, 'befUrlPvRate': None, 'aftUrl': None, 'aftUrlType': None, 'aftUrlLevel': None, 'aftUrlName': None, 'aftUrlPv': 58, 'aftUrlPvRate': 0.0073, 'etlDate': None}
        # assert response.json()['data']['down'][0] =={'id': None, 'cycleId': '20200817', 'ownCorpStdOrgCode': None, 'stdProdLineVerCode': None, 'monthItvType': None, 'vocation': None, 'url': None, 'urlType': None, 'urlLevel': None, 'urlName': '非凡高清首页', 'befUrl': None, 'befUrlType': None, 'befUrlLevel': None, 'befUrlName': None, 'befUrlPv': 1645, 'befUrlPvRate': 0.3522, 'aftUrl': None, 'aftUrlType': None, 'aftUrlLevel': None, 'aftUrlName': None, 'aftUrlPv': None, 'aftUrlPvRate': None, 'etlDate': None}



if __name__ == '__main__':
    pytest.main(["-sv"])
