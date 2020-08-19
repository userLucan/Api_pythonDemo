#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-19 14:36
# @Author  : 刘开
"""
用户留存
"""

import requests
import pytest
from commen.config import Config

class TestuserRetention():
    @classmethod
    def setup_class(self):
        self.config = Config()

    @classmethod
    def teardown(self):
        print('执行完毕')

    def test_live(self):
        """用户留存日数据校验"""
        url = '/crystalBall-web/page/live?'
        data = {
            "type": "day",
            "from": "20200812",
            "end": "20200819",
            "line": "3",
            "region": "40",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "name":"",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] =={'cycleId': '20200812', 'newCnt': 407, 'retentionRate01': 0.3415, 'retentionRate02': 0.3022, 'retentionRate03': 0.2752, 'retentionRate04': 0.2752, 'retentionRate05': 0.2604, 'retentionRate06': 0.2752, 'retentionRate07': None, 'retentionRate08': None, 'retentionRate09': None}

    def test_live01(self):
        """用户留存周数据校验"""
        url = '/crystalBall-web/page/live?'
        data = {
            "from": "20200708",
            "end": "20200819",
            "line": "3",
            "region": "40",
            "type": "week",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] == {'cycleId': '20200706至20200712', 'newCnt': 4024, 'retentionRate01': 0.4167, 'retentionRate02': 0.374, 'retentionRate03': 0.3514, 'retentionRate04': 0.3355, 'retentionRate05': 0.33, 'retentionRate06': None, 'retentionRate07': None, 'retentionRate08': None, 'retentionRate09': None}

    def test_live02(self):
        """用户留存月数据校验"""
        url = '/crystalBall-web/page/live?'
        data = {
            "from": "202007",
            "end": "202007",
            "line": "3",
            "region": "40",
            "type": "month",
            "url": "http://hd2.hzdtv.tv/template_images/html/new_index/wasuindex.html",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1597814427921",
            "token": self.config.get_value('cookie.conf', 'token', 'token')}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0] =={'cycleId': '202007', 'newCnt': 16310, 'retentionRate01': None, 'retentionRate02': None, 'retentionRate03': None, 'retentionRate04': None, 'retentionRate05': None, 'retentionRate06': None, 'retentionRate07': None, 'retentionRate08': None, 'retentionRate09': None}



if __name__ == '__main__':
    pytest.main(['sv'])