#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-07 13:56
# @Author  : 刘开

import requests
import pytest
from commen.config import Config


class TestAnalysis():
    @classmethod
    def setup_class(cls):
        cls.config = Config()

    @classmethod
    def teardown(cls):
        print('执行完毕')

    def test_Silence(self):
        """校验数据列表"""
        url = '/crystalBall-web/user/Silence'
        data = {
            "cycle_id": 202007,
            "line": 3,
            "region": 10,
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.post(url=self.config.get_value('host.conf', 'host', 'url') + url, data=data)
        execpect = {'from': None, 'end': None, 'line': None, 'region': None, 'cycle_id': '202007',
                    'silence_cnt_1': 183114, 'hb_rate_1': -0.0293, 'silence_cnt_2': 128252, 'hb_rate_2': -0.0162}
        assert response.json()['data']['folders'][0] == execpect


if __name__ == '__main__':
    pytest.main(['-sv'])
